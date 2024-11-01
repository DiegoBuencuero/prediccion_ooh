import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from decimal import Decimal
from ooh.models import EspacioOOH

def entrenar_y_ajustar_precio():
    # Cargar el dataset de ocupaciones
    df = pd.read_csv('ocupaciones.csv')
    df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])
    df['fecha_fin'] = pd.to_datetime(df['fecha_fin'])

    for espacio_nombre in df['espacio'].unique():
        espacio = EspacioOOH.objects.filter(nombre=espacio_nombre).first()
        if espacio is None:
            print(f"No se encontró un espacio con el nombre {espacio_nombre}.")
     
            ocupaciones_espacio = df[df['espacio'] == espacio_nombre]
            serie_ocupacion = ocupaciones_espacio.set_index('fecha_inicio')['tarifa']

            modelo = ARIMA(serie_ocupacion, order=(5, 1, 0))
            modelo_fit = modelo.fit()
            predicciones = modelo_fit.forecast(steps=12)

            demanda_proyectada = sum(predicciones) / len(predicciones)
            if demanda_proyectada > espacio.tarifa:
                nuevo_precio = espacio.tarifa * Decimal(1.20)
            else:
                nuevo_precio = espacio.tarifa * Decimal(0.80)

            espacio.tarifa = nuevo_precio
            espacio.save()
            print(f'Nuevo precio ajustado para {espacio.nombre}: {nuevo_precio}')