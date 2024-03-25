import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos de ECG desde la URL proporcionada
url = "https://raw.githubusercontent.com/RoyGP17/ELECT/main/DATOS-ELECTROCARDIOGRAMA.csvv"
df = pd.read_csv(url)
df = df.drop(labels=0, axis=0)

# Renombrar columnas para una mejor legibilidad
df.columns = ['Tiempo_transcurrido', 'I', 'II', 'III', 'AVR', 'AVL', 'AVF','V1', 'V2', 'V3', 'V4', 'V5', 'V6']

# Convertir columna II a tipo de dato flotante
df["II"] = pd.to_numeric(df["II"], downcast="float", errors='coerce')

# Convertir columna Tiempo_transcurrido a formato datetime
df["Tiempo_transcurrido"] = pd.to_datetime(df["Tiempo_transcurrido"], format="'%M:%S.%f'")

# Calcular estadísticas descriptivas de las columnas numéricas
print(df.describe())

# Visualizar la distribución de los datos con un histograma
df.hist(figsize=(10, 10))
plt.show()  

# Visualizar la distribución de los datos con un histograma
ax = df.hist(figsize=(10, 10))
for axis in ax.flatten():
    axis.set_xlabel("Valor")
    axis.set_ylabel("Frecuencia")
plt.show()


# Visualizar la distribución de los datos con un boxplot
df.boxplot(figsize=(10, 10))
plt.show()
# Visualizar la distribución de los datos con un boxplot
ax = df.boxplot(figsize=(10, 10))
ax.set_xlabel("Columna")
ax.set_ylabel("Valor")
plt.show()

