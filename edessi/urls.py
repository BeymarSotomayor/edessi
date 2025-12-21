"""
URL configuration for edessi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from edessi import settings

# Importa tus vistas personalizadas de login/logout
from app.administrador.views import CustomLogoutView, login_view

urlpatterns = [
    # Redefinir admin para que lleve al login custom
    path("admin", login_view, name="login"),

    # Mantener admin de Django en otra ruta
    path("admin-django/", admin.site.urls),

    # Logout
    path("logout/", CustomLogoutView.as_view(), name="logout"),

    # Portal web
    path("", include("app.portal.urls")),

    # Admin personalizado
    path("", include("app.administrador.urls")),

    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
