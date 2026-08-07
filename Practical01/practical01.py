import numpy as np
import matplotlib.pyplot as plt

Fs = 1000          # Sampling Frequency (Hz)
Fc = 10            # Signal Frequency (Hz)
T = 1              # Duration (seconds)

t = np.arange(0, T, 1/Fs)

signal = np.sin(2 * np.pi * Fc * t)

noise = 0.4 * np.random.randn(len(signal))

noisy_signal = signal + noise

normalized_signal = (noisy_signal - np.min(noisy_signal)) / \
                    (np.max(noisy_signal) - np.min(noisy_signal))

window_size = 10

filtered_signal = np.convolve(
    normalized_signal,
    np.ones(window_size) / window_size,
    mode='same'
)

plt.figure(figsize=(12, 10))

# Original Signal
plt.subplot(4, 1, 1)
plt.plot(t, signal, 'b')
plt.title("Original Sinusoidal Signal")
plt.ylabel("Amplitude")
plt.grid(True)

# Noisy Signal
plt.subplot(4, 1, 2)
plt.plot(t, noisy_signal, 'r')
plt.title("Noisy Signal")
plt.ylabel("Amplitude")
plt.grid(True)

# Normalized Signal
plt.subplot(4, 1, 3)
plt.plot(t, normalized_signal, 'g')
plt.title("Normalized Signal")
plt.ylabel("Amplitude")
plt.grid(True)

# Filtered Signal
plt.subplot(4, 1, 4)
plt.plot(t, filtered_signal, 'm')
plt.title("Filtered Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
