from django.db import models

class EspacioOOH(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    tarifa = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Ocupacion(models.Model):
    espacio = models.ForeignKey(EspacioOOH, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_vendido = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.espacio} - {self.fecha_inicio} to {self.fecha_fin}'
    
    
class RegistroAjustePrecio(models.Model):
    espacio = models.ForeignKey('EspacioOOH', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2)
    precio_nuevo = models.DecimalField(max_digits=10, decimal_places=2)
    demanda_proyectada = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.espacio.nombre} - {self.fecha} - {self.precio_nuevo}"