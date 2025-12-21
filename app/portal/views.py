from django.shortcuts import render, get_object_or_404
from app.administrador.models import *
from app.administrador.views import *

def inicio(request):
    return render(request, 'portal/inicio.html')

def about(request):
    return render(request, 'portal/about.html')

def login_view(request):
    return render(request, 'portal/login.html')

def registrar(request):
    return render(request, 'portal/registrar.html')


# def programas(request):
#     return render(request, 'portal/web/programas.html')

# def juegos(request):
#     category = get_object_or_404(
#         Category.objects.prefetch_related("products"),
#         slug="juegos"
#     )

#     return render(
#         request,
#         "portal/web/juegos.html",
#         {"category": category}
#     )
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    company = Company.objects.first()
    
    #company = get_object_or_404(Company, pk=pk)
    return render(request, "portal/web/product_detail.html", {"product": product,"company": company})

def category_detail(request, slug):
    company = Company.objects.first()
    category = get_object_or_404(
        Category.objects.prefetch_related("products"),
        slug=slug
    )
    return render(request, "portal/web/category_list.html", {"category": category,"company": company})

# def juegos(request):
#     return render(request, 'portal/web/juegos.html')

# def audifonos(request):
#     return render(request, 'portal/web/audifonos.html')

# def cargadores(request):
#     return render(request, 'portal/web/cargadores.html')

# def fuentes(request):
#     return render(request, 'portal/web/fuentes.html')

# def ram(request):
#     return render(request, 'portal/web/ram.html')

# def ssd(request):
#     return render(request, 'portal/web/ssd.html')

# def hdd(request):
#     return render(request, 'portal/web/hdd.html')

# def gpu(request):
#     return render(request, 'portal/web/gpu.html')



