#administrador/forms.py
#app.administrador.forms
from django import forms
from .models import Category, Client, Machine, Product,Company,Service
from django.utils import timezone

from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Row, Column, Field
# from crispy_forms.bootstrap import FormActions
from .models import Machine
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field, Div
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate,get_user_model
#from django_intl_tel_input.widgets import IntlTelInputWidget

# 🔹 Editar datos de usuario
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# 🔹 Cambiar contraseña (ya viene listo en Django)
from django.contrib.auth.forms import AuthenticationForm
User = get_user_model()
class CustomAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese su usuario"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Ingrese su contraseña"})
    )

    error_messages = {
        "invalid_login_user": "❌ El usuario no existe.",
        "invalid_login_pass": "❌ La contraseña es incorrecta.",
        "inactive": "⚠️ Esta cuenta está deshabilitada.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                field.widget.attrs["class"] += " is-invalid"

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            try:
                user_obj = User.objects.get(username=username)
            except User.DoesNotExist:
                self.add_error("username", self.error_messages["invalid_login_user"])
                return self.cleaned_data

            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                self.add_error("password", self.error_messages["invalid_login_pass"])
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
    
    
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Contraseña actual",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class ReportFilterForm(forms.Form):
    start_date = forms.DateField(
        label="Fecha inicio",
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control",
            "id": "id_start_date",  # importante para JS
        })
    )
    end_date = forms.DateField(
        label="Fecha final",
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control",
            "id": "id_end_date",  # importante para JS
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and end_date < start_date:
            self.add_error("end_date", "La fecha fin no puede ser menor a la fecha inicio.")


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['logo_img', 'name_company', 'phone_company', 'email', 'address', 'nit']
        labels = {
            'logo_img': 'Logo',
            'name_company': 'Nombre de la Empresa',
            'phone_company': 'Teléfono',
            'email': 'Correo Electrónico',
            'address': 'Dirección',
            
            'nit': 'NIT',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 🔹 Placeholders
        self.fields['logo_img'].widget.attrs['placeholder'] = 'Sube el logo de la empresa'
        self.fields['name_company'].widget.attrs['placeholder'] = 'Ej: Mi Empresa S.R.L.'
        self.fields['phone_company'].widget.attrs['placeholder'] = '76543210'
        self.fields['address'].widget.attrs['placeholder'] = 'Ej: Calle Principal #123, Ciudad'
        self.fields['email'].widget.attrs['placeholder'] = 'Ej: ejemplo@empresa.com'
        #self.fields['location'].widget.attrs['placeholder'] = 'Pega el enlace de GoogleMaps'
        self.fields['nit'].widget.attrs['placeholder'] = 'Ej: 123456789'

# -------- Formularios --------

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nombre',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        # 🔹 Colocar placeholders en campos existentes
        self.fields['name'].widget.attrs['placeholder'] = 'Nombre de la Categoria'
        

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'phone']#, 'email'
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellidos',
            #'email': 'Correo',
            'phone': 'Teléfono',
            
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        # 🔹 Colocar placeholders en campos existentes
        self.fields['name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellidos'
        #self.fields['email'].widget.attrs['placeholder'] = 'ejemplo@gmail.com o example@gmail.com'
        self.fields['phone'].widget.attrs['placeholder'] = 'Ejemplo: +591 12345678'
        
# SERVICE_CHOICES = [
#         ("Instalación de sistema operativo", "Instalación de sistema operativo"),
#         ("Instalación de aplicaciones de Desktop", "Instalación de aplicaciones de Desktop"),
#         ("Reparación de bisagra", "Reparación de bisagra"),
#         ("Limpieza de polvo", "Limpieza de polvo"),
#         ("Cambio de pasta térmica", "Cambio de pasta térmica"),
#         ("Limpieza de cabezal", "Limpieza de cabezal"),
#         ("Mantenimiento de software", "Mantenimiento de software"),
#         ("Cambio de rodillos", "Cambio de rodillos"),
#         ("Cambio de cabezales", "Cambio de cabezales"),
#         ("Cambio de teclado", "Cambio de teclado"),
#         ("Cambio de plug de carga", "Cambio de plug de carga"),
#         ("Cambio de pantalla", "Cambio de pantalla"),
#     ]


ACCESSORY_CHOICES = [
    ("Cargador", "Cargador"),
    ("Cable USB", "Cable USB"),
    ("Mouse", "Mouse"),
    ("Funda", "Funda"),
    ("Teclado", "Teclado"),
]
class MachineForm(forms.ModelForm):
    accessories = forms.MultipleChoiceField(
        choices=ACCESSORY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Accesorios"
    )
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Servicios"
    )
    
    other_accessories = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Especifica los Otros accesorios que dejo el cliente..."}),
        label="Otros accesorios"
    )
    class Meta:
        model = Machine
        fields = ['img_machine','brand','services', 'model', 'detail','problem','status','price_aprox','price_extra','price_descuento','price_fact','price_a_cuenta','saldo','price','delivery_in','diagnostic','accessories' ]#'ticket',, 'position'
        labels = {
            #'ticket': 'Ficha',
            'img_machine': 'Imagen de evidencia de la maquina',
            'description': 'Descripción',
            'brand': 'Marca',
            'model': 'Modelo',
            'detail': 'Detalle',
            'problem': 'Problema',
            #'position': 'Posición',
            'status': 'Estado',
            'price_aprox': 'Precio',
            'price_extra': 'Extra',
            'price_descuento': 'Descuento',
            'price_fact': 'IVA',
            'price': 'Total',

            'price_a_cuenta': 'Precio a cuenta',
            'saldo': 'Saldo',
            'delivery_in': 'Fecha de Entrega',
            'services': 'Servicio', 
            'diagnostic': 'Diagnostico / Solución', 

            'accessories': 'Accesorios',
            #'machine': 'Máquina',
            #'Client': 'cliente',
        }
        current_time = timezone.localtime(timezone.now())  # Ajusta la hora a la zona horaria local
        current_time_str = current_time.strftime('%Y-%m-%dT%H:%M')  # Formato correcto para datetime-local

        widgets = {
            'delivery_in': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',  # para Bootstrap
                    'min': current_time_str,  # Fecha mínima ajustada a la zona horaria local
                },
                format='%Y-%m-%dT%H:%M'  # Formato compatible con datetime-local
            )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['services'].label_from_instance = lambda obj: f"{obj.name} ({obj.price} Bs)"    

        # 🔹 Colocar placeholders en campos existentes
        self.fields['model'].widget.attrs['placeholder'] = 'Modelo del "Equipo de Cómputo"'
        self.fields['detail'].widget.attrs['placeholder'] = 'Detalle del "Equipo de Cómputo" como lo esta entregando el cliente(opcional)'
        self.fields['problem'].widget.attrs['placeholder'] = 'Descripción detallada del problema'
        self.fields['delivery_in'].widget.attrs['placeholder'] = 'Fecha de entrega ej: 01/01/2025'
        self.fields['delivery_in'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['price_aprox'].widget.attrs['placeholder'] = 'Precio aproximado ej: 45'
        self.fields['price'].widget.attrs['placeholder'] = 'Precio final del servicio'
        #self.fields['position'].widget.attrs['placeholder'] = 'Escriba la posición física del "Equipo de Cómputo" 1 al 12'
        # 🔹 que no sea editable
        self.fields['price_aprox'].widget.attrs['readonly'] = True
        self.fields['price'].widget.attrs['readonly'] = True
        self.fields['saldo'].widget.attrs['readonly'] = True

    
        # Si hay accesorios guardados, separar en lista para marcar checkboxes
        if self.instance and self.instance.accessories:
            acc_list = [a.strip() for a in self.instance.accessories.split(',') if a.strip()]
            # Accesorios predefinidos
            self.fields["accessories"].initial = [
                a for a in acc_list if a in dict(ACCESSORY_CHOICES)
            ]
            # Accesorios personalizados
            others = [a for a in acc_list if a not in dict(ACCESSORY_CHOICES)]
            self.fields["other_accessories"].initial = ", ".join(others)
    

    def clean(self):
        cleaned_data = super().clean()
        accessories = cleaned_data.get("accessories", [])
        other = cleaned_data.get("other_accessories", "")

        # ✅ Combinar ambos campos correctamente
        all_acc = list(accessories)  # copia segura
        if other:
            # puede tener varios separados por coma → separamos
            custom = [x.strip() for x in other.split(',') if x.strip()]
            all_acc.extend(custom)

        # Guardar como texto plano separado por comas
        cleaned_data["accessories"] = ", ".join(sorted(set(all_acc)))
        return cleaned_data
    
    # def __init__(self, *args, **kwargs):
    #     super(MachineForm, self).__init__(*args, **kwargs)

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "price"]

    #     # Asignar placeholders
    #     self.fields['model'].widget.attrs['placeholder'] = 'Ej: MX2025'
    #     self.fields['brand'].widget.attrs['placeholder'] = 'Ej: Epson'
    #     self.fields['detail'].widget.attrs['placeholder'] = 'Descripción breve de la máquina'
    #     self.fields['position'].widget.attrs['placeholder'] = 'Ubicación física de la máquina'
        # self.helper = FormHelper()
        # self.helper.form_method = 'post'
        # self.helper.layout = Layout(
        #     Row(
        #         Column(Field('model', css_class='form-control'), css_class='col-md-6'),
        #         Column(Field('brand', css_class='form-select'), css_class='col-md-6'),
        #     ),
        #     Row(
        #         Column(Field('detail', css_class='form-control', rows="3"), css_class='col-12')
        #     ),
        #     Row(
        #         Column(Field('position', css_class='form-control'), css_class='col-md-6'),
        #         Column(Field('img_machine', css_class='form-control'), css_class='col-md-6'),
        #     ),
        # )


    

# class ServiceForm(forms.ModelForm):
#     class Meta:
#         model = Service
#         fields = [
#             'description', 'delivery_in', 'accessories', 'status',
#             'price', 'ticket', 'category', 'machine'#, #'client'#
#         ]
#         labels = {
#             'description': 'Descripción',
#             'delivery_in': 'Fecha de Entrega',
#             'accessories': 'Accesorios',
#             'status': 'Estado',
#             'price': 'Precio',
#             'ticket': 'Ficha',
#             'category': 'Categoria',
#             'machine': 'Máquina',
#             #'Client': 'cliente',
#         }
#     def __init__(self, *args, **kwargs):
#         super(ServiceForm, self).__init__(*args, **kwargs)

#         # Asignar placeholders
#         self.fields['description'].widget.attrs['placeholder'] = 'Descripción detallada del servicio'
#         self.fields['delivery_in'].widget.attrs['placeholder'] = 'fecha de entrega del cliente ej: 01/01/2025'
#         self.fields['accessories'].widget.attrs['placeholder'] = 'Escribe todos los accesorios que dejo el el cliente'
#         self.fields['price'].widget.attrs['placeholder'] = 'Precio del costo del servicio ej: 45'
#         self.fields['ticket'].widget.attrs['placeholder'] = 'N° de ficha'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'detail', 'img_background', 'img_name', 'price']# ,'category']
        labels = {
            'name': 'Nombre',
            'detail': 'Detalle',
            'img_background': 'Imagen Fondo',
            'img_name': 'Imagen Nombre',
            'price': 'Precio',
            #'category': 'Categoría',
        }
