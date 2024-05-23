from django.db import models

# Create your models here.
TIPO_USUARIOS = (
    ("COORDENADOR", "Coordenador"),
    ("PROFESSOR", "Professor"),
)

TIPO_SALAS = ()

class Senai(models.Model):
    titulo = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logo/")
    endereco = models.CharField(max_length=150)
    def __str__(self):
        return self.titulo
    
class Ambiente(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=300)
    sala = models.CharField(max_length=50)
    foto = models.ImageField(upload_to="salas/")
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    cargo = models.CharField(max_length=15, choices=TIPO_USUARIOS)
    def __str__(self):
        return self.nome

class Reserva(models.Model):
    data = models.CharField(max_length=10)
    horario = models.CharField(max_length=10)
    sala = models.CharField(max_length=15, choices=TIPO_SALAS)
    username = models.CharField(max_length=20)