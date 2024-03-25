import numpy as np
import matplotlib.pyplot as plt

#Parámetros del modelo
beta = 0.3   # Tasa de contagio
gamma = 0.1  # Tasa de recuperación

#Condiciones iniciales
S0 = 0.99    # Porcentaje inicial de susceptibles
I0 = 0.01    # Porcentaje inicial de infectados
R0 = 0.00    # Porcentaje inicial de recuperados

#Tiempo de simulación (en días)
t_max = 100
dt = 1
num_steps = int(t_max / dt)

#Arrays para almacenar los resultados
S = np.zeros(num_steps)
I = np.zeros(num_steps)
R = np.zeros(num_steps)
t = np.linspace(0, t_max, num_steps)

#Condiciones iniciales
S[0] = S0
I[0] = I0
R[0] = R0

#Simulación del modelo utilizando el método de Euler
for step in range(1, num_steps):
    dS = -beta * S[step - 1] * I[step - 1]
    dI = beta * S[step - 1] * I[step - 1] - gamma * I[step - 1]
    dR = gamma * I[step - 1]

    S[step] = S[step - 1] + dt * dS
    I[step] = I[step - 1] + dt * dI
    R[step] = R[step - 1] + dt * dR

#Gráfica de los resultados
plt.figure(figsize=(8, 6))
plt.plot(t, S, label='Susceptibles')
plt.plot(t, I, label='Infectados')
plt.plot(t, R, label='Recuperados')
plt.xlabel('Tiempo (días)')
plt.ylabel('Porcentaje de la población')
plt.legend()
plt.title('Modelo SIR de propagación de virus')
plt.grid(True)
plt.show()