import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar datos de ECG desde la URL proporcionada
url = "https://raw.githubusercontent.com/RoyGP17/ELECT/main/DATOS-ELECTROCARDIOGRAMA.csv"
df = pd.read_csv(url)
df = df.drop(labels=0, axis=0)

# Renombrar columnas para una mejor legibilidad
df.columns = ['Tiempo_transcurrido', 'I', 'II', 'III', 'AVR', 'AVL', 'AVF','V1', 'V2', 'V3', 'V4', 'V5', 'V6']

# Convertir columna II a tipo de dato flotante
df["II"] = pd.to_numeric(df["II"], downcast="float", errors='coerce')

# Configuración inicial de la gráfica
plt.figure(figsize=(13, 4))
line, = plt.plot([], [])
plt.xlabel("Tiempo", size=15)

# Función de inicialización para la animación
def init():
    line.set_data([], [])
    return line,

# Función de actualización de la animación
def update(frame):
    x = df["Tiempo_transcurrido"].iloc[:frame]
    y = df["II"].iloc[:frame]
    line.set_data(x, y)
    
    # Establecer los límites del eje x desde 0 hacia adelante
    plt.gca().set_xlim(0, frame)
    
    plt.gca().relim()
    plt.gca().autoscale_view()
    return line,

# Crear la figura y la animación
fig = plt.gcf()
ani = FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True, interval=30)

# Mostrar la animación
plt.show()
