from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from .models import *
from .form import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    products = Products.objects.all()
    itens_por_pagina = 5
    paginador = Paginator(products, itens_por_pagina)  
    pagina = request.GET.get('page')
    try:
        pag_obj = paginador.page(pagina)
    except PageNotAnInteger:
        pag_obj = paginador.page(1)
    except EmptyPage:
        pag_obj = paginador.page(paginador.num_pages)

    is_admin = request.user.groups.filter(name="administradores").exists()
    context = {'products': products, 'pag_obj': pag_obj, 'is_admin': is_admin}
    return render(request, "ecommerce/index.html",context)



def product_editar(request,id):
    product = get_object_or_404(Products,id=id)
   
    if request.method == 'POST':
        form = ProductsForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_listar')
    else:
        form = ProductsForm(instance=product)

    return render(request,'ecommerce/product_form.html',{'form':form})


def product_remover(request, id):
    product = get_object_or_404(Products, id=id)
    product.delete()
    return redirect('admin_listar') 


def product_criar(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ProductsForm()
            return redirect('admin_listar')
    else:
        form = ProductsForm()

    return render(request, "ecommerce/product_form.html", {'form': form})


def product(request, id):
    product = get_object_or_404(Products, id=id)

    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 1))

        if quantidade <= 0:
            messages.error(request, 'Quantidade inválida.')
        elif quantidade > product.quantidade:
            messages.error(request, 'Quantidade solicitada maior que o estoque disponível.')
        else:
            product.quantidade -= quantidade
            product.save()

            total_compra = Decimal(product.preco) * quantidade
            faturamento, created = Faturamento.objects.get_or_create(id=1)
            faturamento.total += total_compra
            faturamento.save()

            messages.success(request, f'Compra realizada com sucesso! Você comprou {quantidade} unidade(s).')
            return redirect('product', id=product.id)

    return render(request, 'ecommerce/product.html', {'product': product})


def product_listar(request, filtro, tipo):
    if tipo=='marca':
        products = Products.objects.filter(marca=filtro)
    if tipo=='categoria':
        products = Products.objects.filter(categoria=filtro)
    itens_por_pagina = 3
    paginador = Paginator(products, itens_por_pagina)  
    pagina = request.GET.get('page')
    try:
        pag_obj = paginador.page(pagina)
    except PageNotAnInteger:
        pag_obj = paginador.page(1)
    except EmptyPage:
        pag_obj = paginador.page(paginador.num_pages)

    context = {'products': products, 'filtro': filtro,  'pag_obj': pag_obj}  
    return render(request, "ecommerce/listar_products.html",context)


def search_product(request):
    nome = None 
    if 'q' in request.GET:
        print('entrou no if')
        termo_pesquisa = request.GET['q']
        print(termo_pesquisa)
        products = Products.objects.buscar_por_nome(termo_pesquisa)
        nome = termo_pesquisa 
    else:
        products = Products.objects.all()

    context = {'products': products, 'nome': nome}
    return render(request, 'ecommerce/listar_products.html', context)

def admin_listar(request, *filtro):
    faturamento = Faturamento.objects.first()
    if filtro is None:
        products = Products.objects.filter(filtro=filtro)
    else:
        products = Products.objects.all()
    itens_por_pagina = 3
    paginador = Paginator(products, itens_por_pagina)  
    pagina = request.GET.get('page')
    try:
        pag_obj = paginador.page(pagina)
    except PageNotAnInteger:
        pag_obj = paginador.page(1)
    except EmptyPage:
        pag_obj = paginador.page(paginador.num_pages)

    context = {'products': products, 'filtro': filtro,  'pag_obj': pag_obj, 'faturamento': faturamento}  
    return render(request, "ecommerce/listar_admin.html",context)

