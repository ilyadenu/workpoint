import numpy as np
from numpy.fft import fftshift, rfft, irfft
from scipy.fft import fft, fftfreq, ifft
from approximation import uf_func
# from frequency_calculation.freq import frequency
import cmath as cm
import matplotlib.pyplot as plt
from frequency_calculation.freq_for_smooth import frequency_for_smooth

fourier_transform = []  # Список значений преобразований Фурье


def fourier_func(f, y_f: list[float], time: list[float]) -> list[float]:
    j = cm.sqrt(-1)
    return y_f*np.exp(j*f*time)


time_for_sin = np.linspace(-5*10e-7, 5*10e-7, 1000)
Uf = (uf_func(11, 12))[0]
dot_value = 1000
yf = fft(uf_func(11, 12)[0])
# yf = fftshift(yf)
# print(np.abs(yf))
xf = fftfreq(dot_value, 1 / frequency_for_smooth)

# plt.plot(xf, np.abs(yf))
# for i in range(len(yf)):
#     if yf[i] == max(yf):
#         print(i)

yf[:2] = 0

# Подстройка для вывода графиков

# yf_0 = np.abs(yf[0])
# yf_100 = np.abs(yf[100])
# yf_200 = np.abs(yf[200])
#
# print('Отношение амплитуды 2 гармоники к 1:', yf_100/yf_0, '\n', 'Отношение амплитуды 3 гармоники к 1:', yf_200/yf_0)

clear_sig = ifft(yf)

# Обратное преобразование Фурье


# t1 = [[y_f, time, quad(fourier_func, -np.inf, np.inf, args=(y_f, time))[0]] for y_f in Uf for time in time_for_sin]
#
# for i in range(len(t1)):
#     fourier_transform.append(t1[i][2])


# Проверка после фильтрации

# yf1 = fft(clear_sig)
# xf1 = fftfreq(dot_value, 1 / frequency)

# plt.ylabel('Интенсивность, Вт/м2')
# plt.xlabel('Время,с')
plt.grid(True)
# plt.plot(xf1, np.abs(yf1))
plt.plot(time_for_sin, clear_sig)
# plt.plot(fourier_transform)
# plt.plot(time_for_sin, cut_signal)
plt.show()
