from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    senha = models.CharField(max_length=15)
    email = models.EmailField()
    foto_perfil = models.ImageField(upload_to='images')
    celular = models.CharField(max_length=11)
    cpf = models.CharField(max_length=14)
    is_admin = models.BooleanField(default=False)
    # endereco = models.CharField(max_length=200)
    # estado = models.CharField(max_length=2, choices=ESTADOS)
    # cep = models.CharField(max_length=9)
    # cidade = models.CharField(max_length=150, default='')
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)

    def save(self, *args, **kwargs):
        novo_usuario = User.objects.create_user(self.nome, self.email, self.senha)
        grupo_clientes, created = Group.objects.get_or_create(name='clientes')
        novo_usuario.groups.add(grupo_clientes)
        super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome +' '+ self.sobrenome

class Administrador(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    senha = models.CharField(max_length=15, default='senha123')
    email = models.EmailField()
    foto_perfil = models.ImageField(upload_to='images')
    cpf = models.CharField(max_length=14)
    celular = models.CharField(max_length=11)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    is_admin= models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        novo_usuario = User.objects.create_user(self.nome, self.email, self.senha)
        novo_usuario.save()
        grupo_administradores, created = Group.objects.get_or_create(name='administradores')
        novo_usuario.groups.add(grupo_administradores)
        super(Administrador, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome +' '+ self.sobrenome
