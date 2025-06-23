from django.contrib import admin
from .models import *

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=('nome','marca','preco','descricao','imagem')

@admin.register(Faturamento)
class FaturamentoAdmin(admin.ModelAdmin):
    list_display=('total',)