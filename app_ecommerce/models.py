from django.db import models

# Create your models here.

class Products(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.nome
