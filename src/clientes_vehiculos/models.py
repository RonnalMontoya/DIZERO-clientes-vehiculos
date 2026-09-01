from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=150)
    identificacion = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=255)
    correo_electronico = models.EmailField()

    def __str__(self):
        return f"{self.identificacion} - {self.nombres}"


class Vehiculo(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="vehiculos",
    )
    placa = models.CharField(max_length=15, unique=True)
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    anio = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=50)
    kilometraje = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"
