import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal simulada
fs = 1000          # Frecuencia de muestreo (Hz)
duration = 10.0    # Duración de la señal (segundos)
num_samples = int(fs * duration)
t = np.linspace(0, duration, num_samples)

# Parámetros de las ondas del ECG
heart_rate = 75    # Latidos por minuto
p_duration = 0.08  # Duración de la onda P en segundos
qrs_duration = 0.06  # Duración de la onda QRS en segundos
t_duration = 0.2   # Duración de la onda T en segundos

# Generar señales para las ondas P, QRS y T
p_wave = np.sin(2 * np.pi * t * (heart_rate / 60))
qrs_wave = -0.5 * np.cos(2 * np.pi * t * (heart_rate / 60)) + np.cos(8 * np.pi * t * (heart_rate / 60))
t_wave = 0.25 * np.sin(2 * np.pi * t * (heart_rate / 60))

# Combinar las ondas para obtener el ECG
ecg_signal = p_wave + qrs_wave + t_wave

# Agregar ruido gaussiano
noise_stddev = 0.03
noise = np.random.normal(0, noise_stddev, num_samples)
ecg_signal_noisy = ecg_signal + noise

# Graficar el ECG simulado
plt.figure(figsize=(10, 4))
plt.plot(t, ecg_signal_noisy, label='ECG Simulado')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Simulación de Señal de ECG Más Realista')
plt.legend()
plt.grid()
plt.show()



