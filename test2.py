import numpy as np, matplotlib.pyplot as plt
from scipy.fftpack import rfft, irfft

n = 2 ** 8
x = np.linspace(0, 2 * np.pi, n)
y = np.sin(x) + np.cos(x * 30)
f0 = rfft(y)
f1 = f0.copy()
f1[:n // 8] = 0
z = irfft(f1)
f, (spectra, signal) = plt.subplots(2, 1, sharey=False)
spectra.plot(x, f0, label='f0')
spectra.plot(x, f1, label='f1')
spectra.legend()
spectra.title.set_text('spectra')
signal.plot(x, y, label='y')
signal.plot(x, z, label='z')
signal.legend()
signal.title.set_text('signal')
plt.legend()
plt.show()