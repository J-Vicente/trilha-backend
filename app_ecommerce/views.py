from django.shortcuts import render
from .models import *
from .form import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request, servico):
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

    context = {'product': product, 'pag_obj': pag_obj}
    return render(request, "ecommerce/index.html",context)



def product_editar(request,id):
    product = get_object_or_404(Products,id=id)
   
    if request.method == 'POST':
        form = ProductsForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_listar')
    else:
        form = ProductsForm(instance=product)

    return render(request,'ecommerce/product_form.html',{'form':form})


def product_remover(request, id):
    product = get_object_or_404(Products, id=id)
    product.delete()
    return redirect('product_listar') 


def product_criar(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ProductsForm()
            return redirect('product_listar')
    else:
        form = ProductsForm()

    return render(request, "ecommerce/product_form.html", {'form': form})


def product(request, id):
    products = get_object_or_404(Products,id=id)
    context ={
        'products':products
    }
    return render(request, "ecommerce/product.html",context)


def product_listar(request, filtro):
    profissional = Profissional.objects.filter(filtro=filtro)
    itens_por_pagina = 3
    paginador = Paginator(profissional, itens_por_pagina)  
    pagina = request.GET.get('page')
    try:
        pag_obj = paginador.page(pagina)
    except PageNotAnInteger:
        pag_obj = paginador.page(1)
    except EmptyPage:
        pag_obj = paginador.page(paginador.num_pages)

    context = {'profissional': profissional, 'filtro': filtro,  'pag_obj': pag_obj}  
    return render(request, "servicos/listar_admin.html",context)


def buscar_produto(request):
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