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


def harmonics_calc(y_value: list) -> list:

    harm_rel = []
    harmonics_list = [h for h in np.abs(y_value) if h > 0.22]
    harmonics_list.sort(reverse=True)
    harm_rel.append(harmonics_list[0])
    j = 0

    for i in range(len(harmonics_list) - 3):
        avg = (harmonics_list[i+j+1] + harmonics_list[i+j+2]) / 2
        harm_rel.append(avg)
        j += 1

    return harm_rel


time_for_sin = np.linspace(-8.1*10e-8, 8.1*10e-8, 1000)
dot_value = 1000

yf = fft(Uf_approx_sinus)
# print(np.abs(yf))

xf = fftfreq(dot_value, 1 / freq)
xf = [i + 1*10e6 for i in xf]

# plt.plot(xf, np.abs(yf))

# Расчет отношения гармоник

h2_h1_rel = harmonics_calc(yf)[1] / harmonics_calc(yf)[0]
h3_h2_rel = harmonics_calc(yf)[2] / harmonics_calc(yf)[1]
h3_h1_rel = harmonics_calc(yf)[2] / harmonics_calc(yf)[0]
# print('Отношение 2 гармоники к 1 = ', h2_h1_rel, '\n',
#       'Отношение 3 гармоники к 2 = ', h3_h2_rel, '\n',
#       'Отношение 3 гармоники к 1 = ', h3_h1_rel)

shift = 16

yf = np.roll(yf, shift)

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
# plt.show()
