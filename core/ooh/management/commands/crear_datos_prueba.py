from django.core.management.base import BaseCommand
from ooh.models import RegistroAjustePrecio, EspacioOOH
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Crear datos de prueba para RegistroAjustePrecio'

    def handle(self, *args, **kwargs):
        # Obtener todos los espacios disponibles
        espacios = EspacioOOH.objects.all()

        if not espacios.exists():
            self.stdout.write(self.style.ERROR('No hay espacios disponibles. Por favor, crea algunos antes de ejecutar este comando.'))
            return

        # Generar datos de prueba
        for i in range(10):
            espacio = random.choice(espacios)  # Elegir un espacio aleatorio
            RegistroAjustePrecio.objects.create(
                espacio=espacio,  # Asignar el espacio
                fecha=date.today() - timedelta(days=i*10),
                precio_anterior=random.uniform(1000, 2000),
                precio_nuevo=random.uniform(1000, 2000),
                demanda_proyectada=random.uniform(500, 1000)
            )

        self.stdout.write(self.style.SUCCESS('Datos de prueba creados exitosamente'))