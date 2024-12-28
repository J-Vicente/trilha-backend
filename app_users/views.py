from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .form import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def editar_cliente(request,id):
    cliente = get_object_or_404(Cliente,id=id)
   
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES,instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UserForm(instance=cliente)

    return render(request,'users/user_form.html',{'form':form})

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = UserForm()
            return redirect('login')
    else:
        form = UserForm()

    return render(request, "users/user_form.html", {'form': form})

# -----------------------------------------------------------------------------------------------------    

