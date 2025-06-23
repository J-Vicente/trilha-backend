from django.db import models

# Create your models here.
class ProductsManager(models.Manager):
    def buscar_por_nome(self, termo):
        return self.filter(nome__icontains=termo)

class Products(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    preco = models.FloatField()
    quantidade = models.IntegerField(default=0)    
    categoria = models.CharField(max_length=100, default='')
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(upload_to='images')
    objects = ProductsManager()
    
    def __str__(self):
        return self.nome


class Faturamento(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Faturamento: R$ {self.total}'