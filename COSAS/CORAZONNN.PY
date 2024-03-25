import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar datos de ECG desde la URL proporcionada
url = "https://raw.githubusercontent.com/RoyGP17/ELECT/main/DATOS-ELECTROCARDIOGRAMA.csv"
df = pd.read_csv(url)
df = df.drop(labels=0, axis=0)

# Renombrar columnas para una mejor legibilidad
df.columns = ['Tiempo_transcurrido', 'I','II','III','AVR','AVL','AVF','V1','V2','V3','V4','V5','V6']

# Convertir columna II a tipo de dato flotante
df["II"] = pd.to_numeric(df["II"], downcast="float", errors='coerce')

# Convertir columna Tiempo_transcurrido a formato datetime
df["Tiempo_transcurrido"] = pd.to_datetime(df["Tiempo_transcurrido"], format="'%M:%S.%f'")

# Configuración inicial de la gráfica
plt.figure(figsize=(13, 4))
line, = plt.plot([], [])
plt.ylabel("Voltios (mV)", size=10)
plt.xlabel("Tiempo (s)", size=10)

# Función de inicialización para la animación
def init():
    line.set_data([], [])
    return line,

# Función de actualización de la animación
def update(frame):
    x = df["Tiempo_transcurrido"].iloc[:frame]
    y = df["II"].iloc[:frame]
    line.set_data(x, y)
    plt.gca().relim()
    plt.gca().autoscale_view()
    return line,

# Intervalo extremadamente bajo para máxima velocidad de dibujo
interval = 0.5 # Intervalo de 0.5 ms

# Crear la figura y la animación
fig = plt.gcf()
ani = FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True, interval=interval)

# Mostrar la animación
plt.show()


