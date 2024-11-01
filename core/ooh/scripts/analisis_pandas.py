import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# data = {
# 'Producto': ['Pantalla A', 'Pantalla B', 'Pantalla C'],
#     'Ubicación': ['Centro', 'Norte', 'Sur'],
#     'Tarifa': [500, 750, 620],
#     'Disponible': [True, False, True]
# }

# #df = pd.DataFrame(data) # transformo un diccionario en una tabla
# print("Directorio actual:", os.getcwd()) # saber cual es la ruta
#csv_path = os.path.join(os.path.dirname(__file__), 'ocupaciones.csv') 
# csv_path = 'core/ooh/scripts/ocupaciones.csv'
# try:
#     df = pd.read_csv(csv_path)
#     print("contenido del archivo")
#     print(df)
# except FileNotFoundError:
#     print("Error: El archivo 'ocupaciones.csv' no se encuentra.")


# print("\nDescripción estadística de los datos numéricos:")
# print(df.describe())

# Ruta al archivo CSV
csv_path = os.path.join(os.path.dirname(__file__), 'ocupaciones.csv')
df = pd.read_csv(csv_path)

# Crear la carpeta 'static/images' dentro de 'core' si no existe
output_dir = os.path.join(os.path.dirname(__file__), '../../static/images')
os.makedirs(output_dir, exist_ok=True)

# Estilo de gráfico
plt.style.use('ggplot')

# 1. Histograma para la columna 'tarifa'
plt.figure(figsize=(10, 5))
plt.hist(df['tarifa'], bins=20, alpha=0.7, label='Tarifa')
plt.xlabel('Tarifa')
plt.ylabel('Frecuencia')
plt.title('Distribución de Tarifa')
plt.legend()
plt.savefig(os.path.join(output_dir, 'tarifa_histograma.png'))  # Guardar el gráfico en 'static/images'
plt.close()

# 2. Histograma para la columna 'precio_vendido'
plt.figure(figsize=(10, 5))
plt.hist(df['precio_vendido'], bins=20, alpha=0.7, color='orange', label='Precio Vendido')
plt.xlabel('Precio Vendido')
plt.ylabel('Frecuencia')
plt.title('Distribución de Precio Vendido')
plt.legend()
plt.savefig(os.path.join(output_dir, 'precio_vendido_histograma.png'))  # Guardar el gráfico en 'static/images'
plt.close()

# 3. Box Plot para comparar 'tarifa' y 'precio_vendido'
plt.figure(figsize=(8, 6))
sns.boxplot(data=df[['tarifa', 'precio_vendido']])
plt.title('Box Plot de Tarifa y Precio Vendido')
plt.ylabel('Valor')
plt.savefig(os.path.join(output_dir, 'tarifa_precio_boxplot.png'))  # Guardar el gráfico en 'static/images'
plt.close()