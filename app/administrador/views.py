# app/administrador/views.py
# app.administrador.views
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Category, Client, Machine, Product,Company,Service
from .forms import CategoryForm, ClientForm, MachineForm, ProductForm,CompanyForm,ReportFilterForm,ServiceForm,CustomAuthenticationForm
from .utils import get_client_ip
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
import qrcode
import hashlib
from io import BytesIO
from django.http import HttpResponse

import os
import tempfile
from django.conf import settings
from django.http import FileResponse
from django.template.loader import render_to_string
from django.db.models import Sum,Count
from weasyprint import HTML, CSS
from .forms import ReportFilterForm
from .models import Machine

from datetime import datetime, time
from django.utils import timezone
from django.utils.timezone import localtime
from django.db.models.functions import TruncMonth, TruncDay


from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


#@login_required(login_url="login")
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("admin")  # tu panel de inicio
    else:
        form = CustomAuthenticationForm()

    return render(request, "admin/login_admin.html", {"form": form})


        

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

# DASHBOARD protegido
class AdminHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Datos actuales
        context["clients"] = Client.objects.all()
        context["form"] = ClientForm()

        context["total_clients"] = Client.objects.count()
        context["total_machines"] = Machine.objects.count()
        context["total_products"] = Product.objects.count()
        context["total_categories"] = Category.objects.count()
        context["total_services"] = Service.objects.count()

        # Ingresos
        total_machine_price = Machine.objects.aggregate(total=Sum("price"))["total"] or 0
        total_services_price = Service.objects.aggregate(total=Sum("price"))["total"] or 0
        context["total_income"] = total_machine_price

        # Máquinas por estado
        estados = [
            "Recibido", "En Revisión", "Diagnóstico", "Reparación",
            "Pausado", "Cancelado", "En Proceso", "Terminado",
            "Por Entregar", "Entregado"
        ]
        for estado in estados:
            context[f"machines_{estado.lower().replace(' ', '_')}"] = Machine.objects.filter(status=estado).count()

        # Servicios más requeridos (ordenados por cantidad de máquinas que lo tienen)
        top_services = (
            Service.objects.annotate(num_machines=Count("machines"))
            .filter(num_machines__gt=0)
            .order_by("-num_machines")[:14]  # 👈 los 6 más usados
        )
        context["service_labels"] = [s.name for s in top_services]
        context["service_counts"] = [s.num_machines for s in top_services]
        
        today = timezone.localtime().date()

        # ⏳ Rango de día
        start_of_day = timezone.make_aware(datetime.combine(today, time.min))
        end_of_day = timezone.make_aware(datetime.combine(today, time.max))

        # 📅 Rango de mes
        start_of_month = timezone.make_aware(
            datetime.combine(today.replace(day=1), time.min)
        )
        end_of_month = timezone.make_aware(
            datetime.combine(today.replace(day=today.day), time.max)
        )

        estados_validos =["Entregado"]# ["Terminado", "Por Entregar", "Entregado"]

        # 💰 Ingreso total del día (máquinas en esos estados)
        daily_income = (
            Machine.objects.filter(
                status__in=estados_validos,
                created_at__range=(start_of_day, end_of_day),
            ).aggregate(total=Sum("price"))["total"] or 0
        )

        # 💰 Ingreso total del mes (máquinas en esos estados)
        monthly_income = (
            Machine.objects.filter(
                status__in=estados_validos,
                created_at__range=(start_of_month, end_of_month),
            ).aggregate(total=Sum("price"))["total"] or 0
        )

        # Agregar al contexto
        context["daily_income_total"] = float(daily_income)
        context["monthly_income_total"] = float(monthly_income)
        

        return context


class ProtectedView(LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'next'



import io
from django.http import FileResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.utils import timezone
from datetime import datetime, time
from django.db.models import Sum
from decimal import Decimal, ROUND_HALF_UP
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash

from .forms import UserUpdateForm, CustomPasswordChangeForm

@login_required
def profile_settings(request):
    # Inicializar formularios
    u_form = UserUpdateForm(instance=request.user)
    form = CustomPasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if 'save_profile' in request.POST:  # Botón de editar perfil
            u_form = UserUpdateForm(request.POST, instance=request.user)
            if u_form.is_valid():
                u_form.save()
                messages.success(request, "✅ Datos actualizados correctamente")
                return redirect('profile_settings')

        elif 'change_password' in request.POST:  # Botón de cambiar contraseña
            form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Mantener sesión activa
                messages.success(request, "🔑 Contraseña actualizada correctamente")
                return redirect('profile_settings')

    return render(request, 'users/profile_settings.html', {
        'u_form': u_form,
        'form': form
    })


@login_required(login_url="login")
def report_machines_pdf(request):
    total = None
    machines = Machine.objects.all()

    form = ReportFilterForm(request.GET or None)
    if form.is_valid():
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]

        start_datetime = timezone.make_aware(datetime.combine(start_date, time.min))
        end_datetime = timezone.make_aware(datetime.combine(end_date, time.max))

        machines = Machine.objects.filter(created_at__range=(start_datetime, end_datetime))
        total = machines.aggregate(total_price=Sum("price"))["total_price"]
        total = Decimal(total or 0).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # ⚙️ Verifica si el usuario quiere ver el HTML directamente
    if request.GET.get("view") == "html":
        return render(request, "admin/report/_report_.html", {"machines": machines, "total": total})

    # 📄 Generar PDF si no hay ?view=html
    html_string = render_to_string(
        "admin/report/_report_.html",
        {"machines": machines, "total": total}
    )

    pdf_file = io.BytesIO()
    HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(
        target=pdf_file,
        stylesheets=[CSS("https://cdn.jsdelivr.net/npm/bootswatch@5.3.3/dist/lumen/bootstrap.min.css")]
    )
    pdf_file.seek(0)

    return FileResponse(pdf_file, as_attachment=False, filename="reporte_maquinas.pdf")

@login_required(login_url="login")
def machine_report_list(request):
    total = None
    machines = Machine.objects.all()

    form = ReportFilterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]

        # 🔹 Igual aquí usamos rango completo
        start_datetime = timezone.make_aware(datetime.combine(start_date, time.min))
        end_datetime = timezone.make_aware(datetime.combine(end_date, time.max))

        machines = Machine.objects.filter(
            created_at__range=(start_datetime, end_datetime)
        )

        machines = machines.filter(created_at__range=(start_datetime, end_datetime))
        total = machines.aggregate(total_price=Sum("price"))["total_price"] or 0.00
    else:
        form = ReportFilterForm()

    return render(request, "admin/machine/machine_list.html", {
        "form": form,
        "machines": machines,
        "total": total,
    })

    
#===========categoria===========

# LISTA categoria
@login_required(login_url="login")
def category_list(request):
    categories = Category.objects.all()
    form = CategoryForm()
    return render(request, "admin/categories/category_list.html", 
    {"categories": categories, "form": form})
def category_product(request, pk):
    # Traer el cliente o mostrar 404 si no existe
    category = get_object_or_404(Category, pk=pk)

    # Filtrar las máquinas que pertenecen a este cliente
    products = Product.objects.filter(category__id=pk)

    # Renderizar con contexto
    return render(
        request,
        "admin/categories/category_product.html",
        {
            "products": products,
            "category": category
        }
    )



# CREAR
@login_required(login_url="login")
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return JsonResponse({
                "success": True,
                "id": category.id,
                "name": category.name,
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    form = CategoryForm()
    return render(request, "admin/categories/category_create_modal.html", {"form": form})


# EDITAR
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "success": True,
                "message": "Categoría actualizada correctamente",
                "data": {
                    "id": category.id,
                    "name": category.name,
                }
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    form = CategoryForm(instance=category)
    return render(request, "admin/categories/category_edit_modal.html", {"form": form, "category": category})

@login_required(login_url="login")
# ELIMINAR
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category_id = category.id
        name = category.name

        if category.products.exists():  # porque en Product → related_name="products"
            return JsonResponse({
                "success": False,
                "message": f"❌ No puedes eliminar la categoría '{name}' porque tiene productos registrados.",
                "id": category_id
            })

        category.delete()
        return JsonResponse({
            "success": True,
            "message": f"Categoría {name} eliminada",
            "id": category_id
        })

    return render(request, "admin/categories/category_delete_modal.html", {"category": category})



# -------- Clientes --------
class ClientListView(ProtectedView, ListView):
    model = Client
    template_name = "admin/clients/client_list.html"
    context_object_name = "clients"
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = ClientForm()
        return ctx


class ClientCreateView(ProtectedView, CreateView):
    model = Client
    form_class = ClientForm
    template_name = "admin/clients/client_create_modal.html"  # 🔹 Nuevo template
    
    def form_valid(self, form):
        client = form.save()
        return JsonResponse({
            "success": True,
            "message": f"Cliente {client.name} {client.last_name} creado correctamente.",
            "id": client.id,
            "name": client.name,
            "last_name": client.last_name,
            "phone": client.phone or "",
            "email": client.email or ""
        })
    
    def form_invalid(self, form):
        return JsonResponse({
            "success": False,
            "errors": form.errors
        })





from django.views.decorators.http import require_POST
@require_POST
def calcular_precio_ajax(request):
    """
    Calcula el precio total, saldo y devolución sin guardar,
    incluyendo el total de los servicios seleccionados (ManyToMany).
    """
    try:
        from app.administrador.models import Service  # ajusta el import según tu estructura
        price = Decimal(request.POST.get("price") or 0)
        #price_aprox = Decimal(request.POST.get("price_aprox") or 0)
        price_extra = Decimal(request.POST.get("price_extra") or 0)
        price_descuento = Decimal(request.POST.get("price_descuento") or 0)
        price_fact = request.POST.get("price_fact") in ["true", "True", "on", "1"]
        price_a_cuenta = Decimal(request.POST.get("price_a_cuenta") or 0)

        # ✅ Sumar precios de servicios seleccionados
        service_ids = request.POST.getlist("services[]")
        total_services = Decimal("0.00")
        if service_ids:
            total_services = Service.objects.filter(id__in=service_ids).aggregate(
                total=Sum("price")
            )["total"] or Decimal("0.00")

        # --- 💰 Lógica igual que el modelo ---
        base_price = (
            total_services +  # 👈 incluye suma de servicios
            #(price_aprox or Decimal(0)) +
            (price_extra or Decimal(0)) -
            (price_descuento or Decimal(0))
        )

        if price_fact:
            iva_factor = Decimal("1") + (Decimal("16") / Decimal("84"))
            total = base_price * iva_factor
        else:
            total = base_price

        total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if total < 0:
            total = Decimal("0.00")

        saldo = total - price_a_cuenta
        saldo = saldo.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        devolucion = Decimal("0.00")
        if saldo < 0:
            devolucion = abs(saldo).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            saldo = Decimal("0.00")

        return JsonResponse({
            "success": True,
            "price": float(total),
            "saldo": float(saldo),
            "devolucion": float(devolucion),
            "total_services": float(total_services),
        })

    except Exception as e:
        return JsonResponse({
            "success": False,
            "error": str(e),
        })

@login_required  # Protege la vista, como lo hace ProtectedView
def list_client_machine(request, pk):
    client = get_object_or_404(Client, pk=pk)
    machines = Machine.objects.filter(client__id=pk)
    company = Company.objects.first()
    data_company = f"""{company.name_company}\n{company.address}\n{company.phone_company}\n{company.email}\n{company.nit}"""
    secret = "Empresa de Desarrollo de Software y Servicios Informáticos"
    hash_firma = hashlib.sha256((data_company + secret).encode('utf-8')).hexdigest()
    context = {
        "client": client,
        "machines": machines,
        "hash_firma": hash_firma
    }
    return render(request, "admin/machine/machine_client_list.html", context)

# -------- Máquinas --------

class MachineListView(ProtectedView, ListView):
    model = Machine
    template_name = "admin/machine/machine_list.html"
    context_object_name = "machines"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MachineForm()  # formulario vacío para el modal "crear"
        return context


class MachineCreateView(ProtectedView, CreateView):
    model = Machine
    form_class = MachineForm
    template_name = "admin/machine/machine_form.html"
    success_url = reverse_lazy("machine_list")

    
class MachineUpdateView(ProtectedView, UpdateView):
    model = Machine
    form_class = MachineForm
    template_name = "admin/machine/machine_form.html"
    success_url = reverse_lazy("machine_list")
    

class MachineDeleteView(ProtectedView, DeleteView):
    model = Machine
    template_name = "admin/machine/machine_confirm_delete.html"
    def get_success_url(self):
        client_id = self.object.client.id  # Asegúrate de que la máquina tenga relación con cliente
        return reverse_lazy("client_machine_list", kwargs={"pk": client_id})





def add_machine(request, id_cliente):
    client = get_object_or_404(Client, pk=id_cliente)  # recupera el cliente

    if request.method == "POST":
        #print(request.POST)
        form = MachineForm(request.POST, request.FILES)
        if form.is_valid():
            machine = form.save(commit=False)  # crea pero no guarda aún
            machine.client = client            # asigna el cliente
            machine.save()                     # guarda en la BD
            return JsonResponse({"success": True, "message": "Máquina registrada correctamente"})
        else:
            return JsonResponse({"success": True, "errors": form.errors}, status=400)
    else:
        form = MachineForm()

    return render(
        request,
        "admin/machine/add_machine.html",
        {"form": form, "client": client}
    )
def add_product(request, id_categoria):
    category = get_object_or_404(Category, pk=id_categoria)  # recupera el categoria

    if request.method == "POST":
        #print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)  # crea pero no guarda aún
            product.category = category            # asigna el cliente
            product.save()                     # guarda en la BD
            return JsonResponse({"success": True, "message": "Máquina registrada correctamente"})
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    else:
        form = ProductForm()

    return render(
        request,
        "admin/products/add_product.html",
        {"form": form, "category": category}
    )

# esto es para obtener la direccion IP de la maquina que haga alguna acción




def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == "POST":
        ip = get_client_ip(request)  #  Obtener IP
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            print(f" Cliente {client.name} {client.last_name} editado desde IP: {ip}")
            return JsonResponse({
                "success": True,
                "message": f"Cliente actualizado correctamente (IP: {ip})",
                "data": {
                    "id": client.id,
                    "name": client.name,
                    "last_name": client.last_name,
                    "phone": client.phone,
                    "ip": ip
                }
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    else:  # GET
        form = ClientForm(instance=client)
        return render(request, "admin/clients/client_edit_modal.html", {"form": form, "client": client})

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == "POST":
        ip = get_client_ip(request)  # ✅ Obtener la IP
        client_id = client.id
        name = client.name
        last_name = client.last_name

        # 🔎 Verificar si el cliente tiene máquinas registradas
        if client.clients.exists():  # porque en Machine pusiste related_name="clients"
            return JsonResponse({
                "success": False,
                "message": f"❌ No puedes eliminar al cliente '{name} {last_name}' porque tiene máquinas registradas.",
                "id": client_id,
                "ip": ip
            })
        # 🔥 Registrar en logs o consola
        print(f"⚠️ Cliente eliminado por IP: {ip}")

        client.delete()
        return JsonResponse({
            "success": True,
            "message": f"El cliente {name} {last_name} fue eliminado (IP: {ip}).",
            "id": client_id,
            "ip": ip
        })

    return render(request, 'admin/clients/client_delete_modal.html', {'client': client})

def machine_detail(request, pk):
    # client = get_object_or_404(Client, pk=client_id)
    machine = get_object_or_404(Machine, pk=pk)#, client=client)
    return render(request, "admin/machine/machine_detail.html", {
        # "client": client,
        "machine": machine,
    })
def machine_detail_client(request,client_id, pk):
    client = get_object_or_404(Client, pk=client_id)
    machine = get_object_or_404(Machine, pk=pk, client=client)
    return render(request, "admin/machine/machine_detail.html", {
        "client": client,
        "machine": machine,
    })
def machine_delete_modal(request, pk):
    machine = get_object_or_404(Machine, pk=pk)

    if request.method == "POST":
        ip = get_client_ip(request)  # ✅ Obtener la IP
        machine_id = machine.id
        brand = machine.brand
        model = machine.model

        print(f"⚠️ Máquina eliminada por IP: {ip}")

        machine.delete()
        return JsonResponse({
            "success": True,
            "message": f"La máquina {brand} {model} fue eliminada (IP: {ip}).",
            "id": machine_id,
            "ip": ip
        })

    return render(request, 'admin/machine/machine_delete_modal.html', {'machine': machine})

def machine_edit_modal(request, pk):
    machine = get_object_or_404(Machine, pk=pk)

    # 🧩 Condiciones de bloqueo según estado
    bloquear_todo = machine.status == 'Entregado'
    #bloquear_parcial = machine.status == 'Terminado'
    bloquear_detail_y_accessories = machine.status in ['Reparación', 'Cancelado','Por Entregar']

    if request.method == "POST":
        # 🛑 Si está entregado, no se permite editar nada
        if bloquear_todo:
            return JsonResponse({
                "success": False,
                "message": "No se puede editar una máquina en estado 'Entregado'."
            })

        # 🛑 Si está terminado y se intenta editar algo diferente de status
        """ if bloquear_parcial and 'status' not in request.POST:
            return JsonResponse({
                "success": False,
                "message": "⚠️ Solo se permite cambiar el estado de una máquina 'Terminada'."
            }) """

        ip = get_client_ip(request)  # ✅ Obtener la IP

        # ⚙️ Convertir los checkboxes seleccionados en una lista antes de guardar
        form = MachineForm(request.POST, request.FILES, instance=machine)

        if form.is_valid():
            machine = form.save()
            print(f"✅ Máquina {machine.brand} {machine.model} editada desde IP: {ip}")
            return JsonResponse({
                "success": True,
                "message": f"Máquina actualizada correctamente (IP: {ip})",
                "data": {
                    "id": machine.id,
                    "ticket": machine.ticket,
                    "brand": machine.brand,
                    "model": machine.model,
                    "detail": machine.detail,
                    "problem": machine.problem,
                    "position": machine.position,
                    "accessories": machine.accessories,
                    "status": machine.status,
                    "price_aprox": float(machine.price_aprox) if machine.price_aprox else None,
                    "price": float(machine.price) if machine.price else None,
                    "created_at": machine.created_at.strftime("%Y/%m/%d %H:%M") if machine.created_at else None,
                    "delivery_in": machine.delivery_in.strftime("%Y/%m/%d %H:%M") if machine.delivery_in else None,
                    "client": str(machine.client) if machine.client else None,
                    "img_machine_url": machine.img_machine.url if machine.img_machine else None,
                    "ip": ip
                }
            })
        else:
            return JsonResponse({
                "success": False,
                "errors": form.errors
            })

    else:  # GET → renderizar modal
        # ✅ Cargar accesorios separados por coma como lista
        initial = {}
        if machine.accessories:
            initial['accessories'] = [x.strip() for x in machine.accessories.split(',') if x.strip()]

        form = MachineForm(instance=machine, initial=initial)

        # 🔒 Si está en "Terminado" → bloquear todos los campos menos 'status'
        """ if bloquear_parcial:
            for name, field in form.fields.items():
                if name != 'status':
                    field.widget.attrs['readonly'] = True """

        # 🔒 Si está en "Reparación" o "Cancelado" → bloquear solo 'detail' y 'accessories'
        if bloquear_detail_y_accessories:
            for name, field in form.fields.items():
                if name == 'detail':
                    field.widget.attrs['readonly'] = True
                elif name == 'accessories':
                    field.widget.attrs['onclick'] = "return false;"  # 🔒 evita cambios
                    field.widget.attrs['style'] = "pointer-events:none; opacity:0.6;"  # 💄 visual

        # 🔒 Si está en "Entregado" → bloquear todos los campos
        if bloquear_todo:
            for name, field in form.fields.items():
                if name == 'accessories':
                    field.widget.attrs['onclick'] = "return false;"
                    field.widget.attrs['style'] = "pointer-events:none; opacity:0.6;"
                elif name == 'services':
                    field.widget.attrs['onclick'] = "return false;"
                    field.widget.attrs['style'] = "pointer-events:none; opacity:0.6;"  # 💄 visual
                elif name == 'model':
                    field.widget.attrs['onclick'] = "return false;"
                    field.widget.attrs['style'] = "pointer-events:none; opacity:0.6;"  # 💄 visual
                elif name == 'brand':
                    field.widget.attrs['onclick'] = "return false;"
                    field.widget.attrs['style'] = "pointer-events:none; opacity:0.6;"  # 💄 visual
                elif name == 'problem':
                    field.widget.attrs['readonly'] = True
                elif name == 'delivery_in':
                    field.widget.attrs['readonly'] = True
                elif name == 'position':
                    field.widget.attrs['readonly'] = True
                elif name == 'detail':
                    field.widget.attrs['readonly'] = True
                elif name == 'price_aprox':
                    field.widget.attrs['readonly'] = True
                elif name == 'price':
                    field.widget.attrs['readonly'] = True
                elif name == 'status':
                    field.widget.attrs['onclick'] = "return false;"
                    field.widget.attrs['style'] = "pointer-events:none; opacity:0.6;"  # 💄 visual
                elif name == 'img_machine':
                    field.widget.attrs['onclick'] = "return false;"
                    field.widget.attrs['style'] = "pointer-events:none; opacity:0.6;"  # 💄 visual
                elif name == 'client':
                    field.widget.attrs['readonly'] = True
                elif name == 'ticket':
                    field.widget.attrs['readonly'] = True
                    field.widget.attrs['onclick'] = "return false;"
                    field.widget.attrs['style'] = "pointer-events:none; opacity:0.6;"  # 💄 visua
                elif name == 'other_accessories':
                    field.widget.attrs['readonly'] = True
                elif name == 'price_aprox':
                    field.widget.attrs['readonly'] = True
                elif name == 'price_a_cuenta':
                    field.widget.attrs['readonly'] = True
                elif name == 'price_descuento':
                    field.widget.attrs['readonly'] = True
                elif name == 'price_extra':
                    field.widget.attrs['readonly'] = True

        return render(request, "admin/machine/machine_edit_modal.html", {
            "form": form,
            "machine": machine,
        })


def ticket_machine(request, id_machine):
    machine = get_object_or_404(Machine, pk=id_machine)
    company = Company.objects.first()  # Asumiendo solo una empresa
    client_id = machine.client.id  # ✅ Aquí obtenemos el ID del cliente
    return render(request, "admin/machine/ticket_machine.html", {
        "machine": machine,
        "company": company,
        "client_id": client_id  # ✅ Lo pasamos al template
    })


def qr_ticket_machine(request, id_machine):
    machine = get_object_or_404(Machine, pk=id_machine)
    company = Company.objects.first()
    # Construir URL absoluta al ticket
    url_ticket = request.build_absolute_uri(f"/ticket_machine/{machine.id}/")
    # Contenido del QR
    # Formatear fecha en d/m/Y
    fecha_formateada = machine.created_at.strftime("%d/%m/%Y")
    # qr_data = f"""{company.name_company}
    #             NIT: {company.nit}
    #             Tel: {company.phone_company}
    #             Dir: {company.address}
    #             -----------------------
    #             Servicio Nro: {machine.ticket}
    #             Marca: {machine.brand}
    #             Modelo: {machine.model}
    #             Accesorios: {machine.accessories}
    #             fecha: {fecha_formateada}
    #             Verificación: {url_ticket}"""
    qr_data = f""" {url_ticket} """
    #qr_data = f"""WIFI:T:WPA;S:CEICOM-07 bey;P:10545909;;;"""

    # Firma hash
    secret = "EDESSI_2025"
    hash_firma = hashlib.sha256((qr_data + secret).encode('utf-8')).hexdigest()
    #qr_text1 = f"""05tD7E5F5wusz3+y7Ponmu9wcS0oxxJLkMR+IAGuWdgumBT8cACphOysn10dC671vXa3VMIrURoGfqFamAKMfBPykMvKRT9Wr2/JQz+Q5x0nIf/D8HbpaLmVGfEVqHhtdRbOhOKmuvoiZs51sXlGzdHWcJ/AL11C7YbrQCdMEa846SjMkgYynwrQiCyUBY2tJUmwXRggtFUfkHVCYh5kxn2+nUQS0KWwZ5o0RyQTSKsOKfBm0u0vNBp6Q5K9hRhFC2ZJbbOK0Bd/OE8yIpSYUozvSjspTyAlDD1K3pBUFfwct500XBTzwj+eLbajJv11IfNiD59Uvaxa50axAVdY2g==|6c19a2801e74ed3abc3b8be3"""
    # QR final
    #qr_text = f"{qr_data}\n\nFirma: {hash_firma}"
    qr_text = f"{qr_data}"

    img = qrcode.make(qr_text)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")

# LISTA DE PRODUCTOS
@login_required(login_url="login")
def product_list(request):
    products = Product.objects.all()
    form = ProductForm()
    return render(request, "admin/products/product_list.html", {"products": products, "form": form})


# CREAR PRODUCTO
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return JsonResponse({
                "success": True,
                "id": product.id,
                "name": product.name,
                "price": str(product.price) if product.price else "",
                "category": product.category.name if product.category else "",
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    form = ProductForm()
    return render(request, "admin/products/product_create_modal.html", {"form": form})


# EDITAR PRODUCTO
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "success": True,
                "message": "Producto actualizado correctamente",
                "data": {
                    "id": product.id,
                    "name": product.name,
                    "price": str(product.price) if product.price else "",
                    "category": product.category.name if product.category else "",
                }
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    form = ProductForm(instance=product)
    return render(request, "admin/products/product_edit_modal.html", {"form": form, "product": product})


# ELIMINAR
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product_id = product.id
        name = product.name
        product.delete()
        return JsonResponse({
            "success": True,
            "message": f"Producto {name} eliminado",
            "id": product_id
        })

    return render(request, "admin/products/product_delete_modal.html", {"product": product})
@login_required(login_url="login")
def config_company(request):
    company = Company.objects.first()  # Asumiendo que solo hay una empresa
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('config_company')
    else:
        form = CompanyForm(instance=company)

    return render(request, "admin/company/config_company.html", {
        'company': company,
        'form': form
    })


@login_required(login_url="login")
def service_list(request):
    services = Service.objects.all()
    return render(request, "admin/services/service_list.html", {"services": services})


def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            return JsonResponse({
                "success": True,
                "id": service.id,
                "name": service.name,
                "price": str(service.price)
            })
        return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = ServiceForm()
    return render(request, "admin/services/service_create_modal.html", {"form": form})


def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save()
            return JsonResponse({
                "success": True,
                "message": "Servicio actualizado correctamente",
                "data": {"id": service.id, "name": service.name, "price": str(service.price)}
            })
        return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = ServiceForm(instance=service)
    return render(request, "admin/services/service_edit_modal.html", {"form": form, "service": service})


def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        service.delete()
        return JsonResponse({"success": True, "id": pk, "message": "Servicio eliminado"})
    return render(request, "admin/services/service_delete_modal.html", {"service": service})

# @login_required(login_url="login")
# def add_services(request, id_machine):
#     machine = get_object_or_404(Machine, pk=id_machine)  # recupera la máquina

#     if request.method == "POST":
#         form = ServiceForm(request.POST, request.FILES)
#         if form.is_valid():
#             service = form.save(commit=False)  # no guarda aún
#             service.machine = machine          # asigna la máquina al servicio
#             service.client = machine.client    # asigna el cliente (si viene de Machine)
#             service.save()                     # guarda el servicio
#             return JsonResponse({"success": True, "message": "Servicio registrado correctamente"})
#         else:
#             return JsonResponse({"success": False, "errors": form.errors}, status=400)
#     else:
#         form = ServiceForm()

#     return render(
#         request,
#         "admin/services/add_service.html",
#         {"form": form, "machine": machine}
#     )

# from django.views.decorators.csrf import csrf_exempt
# class ClientUpdateView(ProtectedView, UpdateView):
#     model = Client
#     form_class = ClientForm
#     template_name = "admin/clients/client_form.html"
#     success_url = reverse_lazy("client_list")


# class ClientDeleteView(ProtectedView, DeleteView):
#     model = Client
#     template_name = "admin/clients/client_confirm_delete.html"
#     success_url = reverse_lazy("client_list")
# -------- Servicios --------
# class ServiceListView(ProtectedView, ListView):
#     model = Service
#     template_name = "admin/services/service_list.html"
#     context_object_name = "services"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = ServiceForm()  # formulario vacío para el modal "crear"
#         return context


# class ServiceCreateView(ProtectedView, CreateView):
#     model = Service
#     form_class = ServiceForm
#     template_name = "admin/services/service_form.html"
#     success_url = reverse_lazy("service_list")


# class ServiceUpdateView(ProtectedView, UpdateView):
#     model = Service
#     form_class = ServiceForm
#     template_name = "admin/services/service_form.html"
#     success_url = reverse_lazy("service_list")


# class ServiceDeleteView(ProtectedView, DeleteView):
#     model = Service
#     template_name = "admin/services/service_confirm_delete.html"
#     success_url = reverse_lazy("service_list")

# -------- Productos --------
# class ProductListView(ProtectedView, ListView):
#     model = Product
#     template_name = "admin/product/product_list.html"
#     context_object_name = "products"


# class ProductCreateView(ProtectedView, CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = "admin/product/product_form.html"
#     success_url = reverse_lazy("product_list")


# class ProductUpdateView(ProtectedView, UpdateView):
#     model = Product
#     form_class = ProductForm
#     template_name = "admin/product/product_form.html"
#     success_url = reverse_lazy("product_list")


# class ProductDeleteView(ProtectedView, DeleteView):
#     model = Product
#     template_name = "admin/product/product_confirm_delete.html"
#     success_url = reverse_lazy("product_list")

# class CategoryListView(ProtectedView, ListView):
#     model = Category
#     template_name = "admin/categories/category_list.html"
#     context_object_name = "categories"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = CategoryForm()  # formulario vacío para el modal "crear"
#         return context


# class CategoryCreateView(ProtectedView, CreateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = "admin/categories/category_form.html"
#     success_url = reverse_lazy("category_list")


# class CategoryUpdateView(ProtectedView, UpdateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = "admin/categories/category_form.html"
#     success_url = reverse_lazy("category_list")


# class CategoryDeleteView(ProtectedView, DeleteView):
#     model = Category
#     template_name = "admin/categories/category_confirm_delete.html"
#     success_url = reverse_lazy("category_list")


# -------- lista de Máquinas del cliente-------
# class MachineClientViews(ProtectedView, ListView):
#     model = Machine
#     template_name = "admin/machine/machine_client_list.html"
#     context_object_name = "machines"

#     def get_queryset(self):
#         client_id = self.kwargs["pk"]
#         return Machine.objects.filter(client__id=client_id)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         client = get_object_or_404(Client, pk=self.kwargs["pk"])
#         context["client"] = client
#         return context