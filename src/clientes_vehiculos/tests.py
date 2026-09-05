from django.db import IntegrityError, transaction
from django.test import TestCase

from .models import Cliente, Vehiculo


class CP_I02_UnicidadTest(TestCase):

    def test_cp_i02_rechaza_identificacion_y_placa_duplicadas(self):
        cliente_principal = Cliente.objects.create(
            nombres="Dina Tanguila",
            identificacion="0912345678",
            telefono="0991234567",
            direccion="Guayaquil",
            correo_electronico="dina@correo.com",
        )

        Vehiculo.objects.create(
            cliente=cliente_principal,
            placa="ABC1234",
            marca="Toyota",
            modelo="Corolla",
            anio=2022,
            color="Blanco",
            kilometraje=15000,
        )

        # Identificación duplicada
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Cliente.objects.create(
                    nombres="Ronnal Montoya",
                    identificacion="0912345678",
                    telefono="0987654321",
                    direccion="Quito",
                    correo_electronico="ronnal@correo.com",
                )

        self.assertEqual(
            Cliente.objects.filter(identificacion="0912345678").count(),
            1,
        )

        segundo_cliente = Cliente.objects.create(
            nombres="Anthony Rubio",
            identificacion="0923456789",
            telefono="0976543210",
            direccion="Guayaquil",
            correo_electronico="anthony@correo.com",
        )

        # Placa duplicada
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Vehiculo.objects.create(
                    cliente=segundo_cliente,
                    placa="ABC1234",
                    marca="Chevrolet",
                    modelo="Sail",
                    anio=2023,
                    color="Gris",
                    kilometraje=1000,
                )

        self.assertEqual(
            Vehiculo.objects.filter(placa="ABC1234").count(),
            1,
        )