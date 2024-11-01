from django.contrib import admin
from django.urls import path
from ooh import views  # Asegúrate de importar las vistas desde ooh

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('generar-datos/', views.ejecutar_generar_datos),  # Esta URL llama a la vista que ejecuta el comando
    path('extraer-datos/', views.extraer_datos_ocupaciones),
    path('visualizar-cambios-precio/', views.visualizar_cambios_precio, name='visualizar_cambios_precio'),
    path('visualizar-graficos/', views.visualizar_graficos, name='visualizar_graficos'),
    path('ver-espacios/', views.ver_espacios_agosto_octubre, name='ver_espacios'),
]