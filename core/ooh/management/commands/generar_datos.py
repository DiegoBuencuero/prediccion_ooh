from django.core.management.base import BaseCommand
from ooh.models import EspacioOOH, Ocupacion
from datetime import date, timedelta
import random
from decimal import Decimal  # Importa Decimal

class Command(BaseCommand):
    help = 'Genera datos de prueba para Espacios OOH y Ocupaciones'

    def handle(self, *args, **kwargs):
        tipos_espacios = ["Front Light", "Backlight", "Digital Billboard", "LED Screen"]
        ubicaciones = ["Centro", "Norte", "Sur", "Este", "Oeste"]
        clientes = ["Cliente A", "Cliente B", "Cliente C", "Cliente D", "Cliente E", "Cliente F", "Cliente G"]

        # Función para generar una fecha aleatoria
        def generar_fecha():
            inicio = date(2024, 1, 1)
            return inicio + timedelta(days=random.randint(0, 365))

        # Generar 10 espacios OOH aleatorios
        for i in range(10):
            espacio = EspacioOOH(
                nombre=f'{random.choice(tipos_espacios)} {chr(65 + i)}',
                ubicacion=random.choice(ubicaciones),
                tarifa=random.uniform(400, 1500),  # La tarifa se queda como float porque el modelo la convertirá a Decimal
                disponible=random.choice([True, False])
            )
            espacio.save()

        # Generar 100 ocupaciones aleatorias
        espacios = EspacioOOH.objects.all()

        for i in range(100):
            espacio = random.choice(espacios)
            fecha_inicio = generar_fecha()
            fecha_fin = fecha_inicio + timedelta(days=random.randint(10, 30))
            
            # Convertimos el valor random a Decimal
            descuento = Decimal(random.uniform(0, 200))  
            
            ocupacion = Ocupacion(
                espacio=espacio,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                precio_vendido=espacio.tarifa - descuento,  # Ahora restamos Decimal con Decimal
                cliente=random.choice(clientes)
            )
            ocupacion.save()

        self.stdout.write(self.style.SUCCESS('Datos generados exitosamente'))