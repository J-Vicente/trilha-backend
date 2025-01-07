"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app_ecommerce.views import *
from app_users.views import *
from . import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('',index,name='index'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('cadastro/cliente/',cadastro_cliente, name='cadastro_cliente'),
    path('admin/cadastro/admin/', cadastro_admin, name='cadastro_admin'),
    path('admin/', admin.site.urls),
    path('product/<int:id>/',product,name='product'),  
    path('listar/',product_listar,name='product_listar'),  
    path('search_product/',search_product,name='search_product'), 
    path('admin/listar/',admin_listar,name='admin_listar'),
    path('admin/product/',product_criar,name='product_criar'),
    path('admin/product/editar/<int:id>/',product_editar, name='product_editar'),
    path('admin/product/remover/<int:id>/',product_remover,name='product_remover'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
