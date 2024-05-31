from django.db import models

TIPO_USUARIOS = (
    ("COORDENADOR", "Coordenador"),
    ("PROFESSOR", "Professor"),
)

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
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=20)
    username = models.CharField(max_length=20, primary_key=True)
    senha = models.CharField(max_length=20)
    cargo = models.CharField(max_length=15, choices=TIPO_USUARIOS)
    def __str__(self):
        return self.nome

class Reserva(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    sala = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.username} - {self.data} - {self.horario}"
