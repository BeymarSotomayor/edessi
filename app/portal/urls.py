from django.urls import path
from . import views
#from app.administrador.urls import *

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login', views.login_view, name='login'),
    path('registrar', views.registrar, name='registrar'),
    # path('programas', views.programas, name='programas'),
    # path('juegos', views.juegos, name='juegos'),
    path('product/<int:pk>/detail/', views.product_detail, name='product_detail'),
    path("categoria/<slug:slug>/", views.category_detail, name="category_detail"),

    # path('audifonos', views.audifonos, name='audifonos'), 
    # path('cargadores', views.cargadores, name='cargadores'),
    # path('fuentes', views.fuentes, name='fuentes'),
    # path('ram', views.ram, name='ram'),
    # path('ssd', views.ssd, name='ssd'),
    # path('hdd', views.hdd, name='hdd'),
    # path('gpu', views.gpu, name='gpu'),
    path('about', views.about, name='about'),
]
