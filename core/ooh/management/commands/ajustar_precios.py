from django.core.management.base import BaseCommand
from ooh.scripts.train_model import entrenar_y_ajustar_precio

class Command(BaseCommand):
    help = 'Entrena el modelo de ocupación y ajusta los precios de los espacios publicitarios'

    def handle(self, *args, **kwargs):
        entrenar_y_ajustar_precio()
        self.stdout.write(self.style.SUCCESS('Modelo entrenado y precios ajustados correctamente'))