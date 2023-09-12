import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq, irfft, fft, fftfreq, ifft, fftshift, ifftshift
from approximation import Uf_approx_sinus
from freq import frequency
from main import time

dot_value = 35
yf = fft(Uf_approx_sinus)
xf = fftfreq(dot_value, 1 / frequency)

# plt.plot(xf, np.abs(yf))

yf[2:] = 0

# Подстройка для вывода графиков

# yf_0 = np.abs(yf[0])
# yf_100 = np.abs(yf[100])
# yf_200 = np.abs(yf[200])
#
# print('Отношение амплитуды 2 гармоники к 1:', yf_100/yf_0, '\n', 'Отношение амплитуды 3 гармоники к 1:', yf_200/yf_0)

clear_sig = ifft(yf)


# Проверка после фильтрации

# yf1 = fft(clear_sig)
# xf1 = fftfreq(dot_value, 1 / frequency)

plt.ylabel('Интенсивность, Вт/м2')
plt.xlabel('Время,с')
plt.grid(True)
# plt.plot(xf1, np.abs(yf1))
# plt.plot(time, clear_sig)
# plt.show()
