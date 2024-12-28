from django.forms import ModelForm
from django import forms
from .models import *



class UserForm(ModelForm):

    class Meta:       
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'sobrenome' : forms.TextInput(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'celular' : forms.TextInput(attrs={'class': 'form-control' }),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control' }),
            'cpf' : forms.TextInput(attrs={'class': 'form-control' }),
            # 'endereco' : forms.TextInput(attrs={'class': 'form-control' }),
            # 'cep' : forms.TextInput(attrs={'class': 'form-control' }),
            # 'cidade' : forms.TextInput(attrs={'class': 'form-control' }),
            # 'estado' : forms.Select(attrs={'class': 'form-control'}),
            'senha' : forms.TextInput(attrs={'class': 'form-control' }),
        }