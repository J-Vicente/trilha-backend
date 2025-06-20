from django.db import models

# Create your models here.
class ProductsManager(models.Manager):
    def buscar_por_nome(self, termo):
        return self.filter(nome__icontains=termo)

class Products(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(upload_to='images')
    objects = ProductsManager()
    
    def __str__(self):
        return self.nome

