from django.forms import ModelForm
from django import forms
from .models import Products

class ProductsForm(ModelForm):

    class Meta:
        model = Products
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'marca' : forms.TextInput(attrs={'class': 'form-control' }),
            'preco' : forms.NumberInput(attrs={'class': 'form-control' }),
            'descricao' : forms.TextInput(attrs={'class': 'form-control' }),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control' })
        }