from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .form import *
from django.contrib.auth.models import User
from django.contrib.auth import logout


def editar_cliente(request,id):
    cliente = get_object_or_404(Cliente,id=id)
   
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES,instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UserForm(instance=cliente)

    return render(request,'users/cliente_form.html',{'form':form})


def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ClienteForm()
            return redirect('login')
    else:
        form = ClienteForm()

    return render(request, "users/cliente_form.html", {'form': form})


def cadastro_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = AdminForm()
            return redirect('login')
    else:
        form = AdminForm()

    return render(request, "users/admin_form.html", {'form': form})


def perfil(request):    
    cliente = Cliente.objects.filter(nome=request.user.username).first()
    return render(request, "users/perfil.html",{'cliente': cliente})
        
# -----------------------------------------------------------------------------------------------------    
def logout_view(request):
    logout(request)  
    return redirect('index')  