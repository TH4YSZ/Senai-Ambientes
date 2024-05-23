from django.contrib import admin
from .models import Senai, Ambiente, Usuario

# Register your models here.
admin.site.register(Senai)
admin.site.register(Ambiente)
admin.site.register(Usuario)