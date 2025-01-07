from django.contrib import admin
from .models import *


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome','sobrenome','email','foto_perfil','celular','cpf')

@admin.register(Administrador)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display=('nome','sobrenome','email','foto_perfil','cpf')

