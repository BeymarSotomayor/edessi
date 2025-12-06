#administrador/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', views.AdminHomeView.as_view(), name='admin'),  # 👈 este es el que Django busca

    #path('login/', views.login_view, name='login'),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),

    # path('login/', views.CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('machine/', views.machine_report_list, name='machines_report_list'),
    #path('register_machine', views.register_machine, name='register_machine'),
    #path('list_machines', views.list_machines, name='list_machines'),
    # --- Categorías ---
    #path('register_product/', views.register_product, name='register_product'),

    # --- Categorías ---
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('categories/<int:pk>', views.category_product, name='category_product'),

    # path('categories/', views.CategoryListView.as_view(), name='category_list'),
    # path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    # path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    # path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # --- Clientes ---
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client_create'),
    #path('clients/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    #path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),
    #path('clients/<int:pk>/', views.MachineClientViews.as_view(), name='client_machine_list'),
    path('clients/<int:pk>/', views.list_client_machine, name='client_machine_list'),

    path('machines/<int:pk>/edit/', views.machine_edit_modal, name='machine_edit_modal'),
    #path('machines/<int:pk>/service/', views.add_service, name='add_service'),
    path('machines/<int:pk>/delete/', views.machine_delete_modal, name='machine_delete_modal'),

    path("clients/<int:client_id>/machines/<int:pk>/detail/", views.machine_detail_client, name="machine_detai_client"),
    path("machines/<int:pk>/detail/", views.machine_detail, name="machine_detail_client"),


    # --- Máquinas ---
    path('machines/', views.MachineListView.as_view(), name='machine_list'),
    path('machines/create/', views.MachineCreateView.as_view(), name='machine_create'),
    path('machines/<int:pk>/update/', views.MachineUpdateView.as_view(), name='machine_update'),
    path('machines/<int:pk>/delete/', views.MachineDeleteView.as_view(), name='machine_delete'),

    # --- Servicios ---
    # path('services/', views.ServiceListView.as_view(), name='service_list'),
    # path('services/create/', views.ServiceCreateView.as_view(), name='service_create'),
    # path('services/<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service_update'),
    # path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),

    # --- Productos ---
    #path('products/', views.ProductListView.as_view(), name='product_list'),
    # path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    # path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    # path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # --- Vistas personalizadas con FBV ---
    path('add_machine/<int:id_cliente>/', views.add_machine, name='add_machine'),
    path('add_product/<int:id_categoria>/', views.add_product, name='add_product'),
    path("clients/<int:pk>/edit_modal/", views.edit_client, name="client_edit_modal"),
    path("clients/<int:pk>/delete1/", views.delete_client, name="delete_client"),

    # path('add_services/<int:id_machine>/', views.add_services, name='add_services'),
    path('ticket_machine/<int:id_machine>/', views.ticket_machine, name='ticket_machine'),
    path('config/', views.config_company, name='config_company'),
    path('qr_machine/<int:id_machine>/', views.qr_ticket_machine, name='qr_ticket_machine'),
    path("report_machines/pdf/", views.report_machines_pdf, name="report_machines_pdf"),

    path("services/", views.service_list, name="service_list"),
    path("services/create/", views.service_create, name="service_create"),
    path("services/<int:pk>/edit/", views.service_edit, name="service_edit"),
    path("services/<int:pk>/delete/", views.service_delete, name="service_delete"),

    #path('perfil/editar/', views.profile_edit, name='profile_edit'),
    #path('perfil/password/', views.change_password, name='change_password'),
    path('perfil/configuracion/', views.profile_settings, name='profile_settings'),
    path("calcular-precio/", views.calcular_precio_ajax, name="calcular_precio_ajax"),

]



