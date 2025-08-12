import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
R = 1.0  # Resistencia del vaso sanguíneo
C = 1  # Capacidad de almacenamiento del vaso sanguíneo
dt = 0.1  # Incremento de tiempo para la integración (paso temporal)
total_time = 10  # Tiempo total de simulación

# Condiciones iniciales
P0 = 80  # Presión inicial en el vaso sanguíneo
Q0 = 0   # Flujo inicial en el vaso sanguíneo

# Listas para almacenar los resultados
time = np.arange(0, total_time, dt)
P = [P0]
Q = [Q0]

# Simulación del modelo
for t in time[1:]:
    # Ecuaciones del modelo
    dPdt = (Q[-1] - C * P[-1]) / R 
    dQdt = (P[-1] - Q[-1] * R) / C

    # Actualización de las variables
    P.append(P[-1] + dPdt * dt)
    Q.append(Q[-1] + dQdt * dt)

# Gráfica de los resultados
plt.figure(figsize=(10, 5))
plt.plot(time, P, label='Presión')
plt.plot(time, Q, label='Flujo')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Modelo de Presión y Flujo en un Vaso Sanguíneo')
plt.legend()
plt.grid(True)
plt.show()



