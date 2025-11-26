from django.contrib import admin
from .models import Mascota

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','especie','raza','nombre_duenio','peso_kg','estado')
