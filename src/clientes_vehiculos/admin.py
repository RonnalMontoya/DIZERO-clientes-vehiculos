from django.contrib import admin

from .models import Cliente, Vehiculo


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("identificacion", "nombres", "telefono", "correo_electronico")
    search_fields = ("identificacion", "nombres", "correo_electronico")


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("placa", "marca", "modelo", "anio", "cliente")
    search_fields = ("placa", "marca", "modelo", "cliente__identificacion")
