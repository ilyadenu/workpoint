import numpy as np
from numpy.fft import fftshift, rfft, irfft
from scipy.fft import fft, fftfreq, ifft
import cmath as cm
import matplotlib.pyplot as plt

from approximation import Uf_approx_sinus
from frequency_calculation.freq import freq
from main import left, right

fourier_transform = []  # Список значений преобразований Фурье


def fourier_func(f, y_f: list[float], time: list[float]) -> list[float]:
    j = cm.sqrt(-1)
    return y_f*np.exp(j*f*time)


time_for_sin = np.linspace(-8.1*10e-8, 8.1*10e-8, 1000)
dot_value = 1000
yf = fft(Uf_approx_sinus)
# yf = np.array(yf)
# yf = np.roll(yf, 800)
# yf = fftshift(yf)
# print(np.abs(yf))
xf = fftfreq(dot_value, 1 / freq)
# xf = [i + 1*10e6 for i in xf]


# plt.plot(xf, np.abs(yf))
# for i in range(len(yf)):
#     if yf[i] == max(yf):
#         print(i)

shift = 16

yf = np.roll(yf, shift)
plt.plot(xf, np.abs(yf))
yf[:shift] = 0
yf[shift + 1:] = 0
# print(np.abs(yf))


# Подстройка для вывода графиков

# yf_0 = np.abs(yf[0])
# yf_100 = np.abs(yf[100])
# yf_200 = np.abs(yf[200])
#
# print('Отношение амплитуды 2 гармоники к 1:', yf_100/yf_0, '\n', 'Отношение амплитуды 3 гармоники к 1:', yf_200/yf_0)

clear_sig = ifft(yf)
cut_clear_sig = clear_sig[485:515]
cut_time = time_for_sin[485:515]


# for i in range(len(clear_sig)):
#     if i % 2 == 0:
#         clear_sig[i] = -1 * clear_sig[i]

# Обратное преобразование Фурье


# t1 = [[y_f, time, quad(fourier_func, -np.inf, np.inf, args=(y_f, time))[0]] for y_f in Uf for time in time_for_sin]
#
# for i in range(len(t1)):
#     fourier_transform.append(t1[i][2])


# Проверка после фильтрации

yf1 = fft(clear_sig)
xf1 = fftfreq(dot_value, 1 / freq)


plt.title('Очищенный сигнал')
plt.ylabel('Uфп, В')
plt.xlabel('Время, с')
plt.grid(True)
# plt.plot(xf1, np.abs(yf1))
# plt.plot(time_for_sin, clear_sig)
# plt.plot(cut_time, cut_clear_sig)
plt.show()
