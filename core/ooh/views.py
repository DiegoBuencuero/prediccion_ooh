from django.http import HttpResponse
from django.core.management import call_command  
import pandas as pd
from ooh.models import Ocupacion, RegistroAjustePrecio
import matplotlib.pyplot as plt
from django.shortcuts import render
import os
from django.conf import settings 

def ejecutar_generar_datos(request):
    call_command('generar_datos')  
    return HttpResponse("Datos generados exitosamente desde la vista")

def  extraer_datos_ocupaciones(request):
    ocupaciones = Ocupacion.objects.all()

    data = []

    for ocupacion in ocupaciones:
        data.append({
            'espacio': ocupacion.espacio.nombre,
            'ubicacion': ocupacion.espacio.ubicacion,
            'fecha_inicio': ocupacion.fecha_inicio,
            'fecha_fin': ocupacion.fecha_fin,
            'tarifa': ocupacion.espacio.tarifa,
            'precio_vendido': ocupacion.precio_vendido
        })
    df = pd.DataFrame(data)

    df.to_csv('ocupaciones.csv', index=False)

    return HttpResponse("Datos extraídos y guardados en ocupaciones.csv")

def visualizar_cambios_precio(request):
    registros = RegistroAjustePrecio.objects.all().order_by('fecha')

    # Verificar si hay registros en la base de datos
    if not registros.exists():
        return HttpResponse("No hay datos en la base de datos para mostrar.")

    data = {
        'fecha': [registro.fecha for registro in registros],
        'precio_anterior': [registro.precio_anterior for registro in registros],
        'precio_nuevo': [registro.precio_nuevo for registro in registros],
        'demanda_proyectada': [registro.demanda_proyectada for registro in registros],
    }
    
    # Imprimir los datos en la consola para verificar
    print(data)

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(data['fecha'], data['precio_anterior'], label="Precio Anterior")
    plt.plot(data['fecha'], data['precio_nuevo'], label="Precio Nuevo")
    plt.plot(data['fecha'], data['demanda_proyectada'], label="Demanda Proyectada", linestyle='--')
    plt.title("Historial de Ajustes de Precios y Demanda Proyectada")
    plt.xlabel("Fecha")
    plt.ylabel("Precio")
    plt.legend()

    # Guardar el gráfico
    imagen_path = os.path.join(settings.BASE_DIR, 'static', 'cambios_precio.png')
    plt.savefig(imagen_path)

    context = {'imagen_url': '/static/cambios_precio.png'}
    
    return render(request, 'visualizacion.html', context)

def visualizar_graficos(request):
    return render(request, 'visualizacion.html')


def ver_espacios_agosto_octubre(request):
    # Usa la ruta absoluta directamente desde la raíz del proyecto
    csv_path = os.path.join(settings.BASE_DIR, 'ooh/scripts/ocupaciones.csv')
    
    # Cargar el archivo CSV y convertir las fechas
    df = pd.read_csv(csv_path)
    df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])
    df['fecha_fin'] = pd.to_datetime(df['fecha_fin'])

    # Filtrar por meses de agosto y octubre
    alquilados_agosto_octubre = df[(df['fecha_inicio'].dt.month.isin([8, 10])) | (df['fecha_fin'].dt.month.isin([8, 10]))]

    # Convertir a diccionario para enviar a la plantilla
    data = alquilados_agosto_octubre.to_dict(orient='records')
    
    # Renderizar los datos en la plantilla
    return render(request, 'ver_espacios.html', {'data': data})
 