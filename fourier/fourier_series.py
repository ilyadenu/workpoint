import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad

from sinus_calc import graph

f = 1e7
T = 2*np.pi
m = np.arange(0, 4, 1)
freq = 2 * np.pi * f


def func_1(t, k, omega):  # функция для расчёта коэффициента a[k]
    g1 = graph[0][485:530]
    for per in range(len(g1)):
        if t < np.pi:
            z = g1[per]*np.cos(omega * k * t)
        else:
            z = -g1[per] * np.cos(omega * k * t)
    return z


def func_2(t, k, omega):  # функция для расчёта коэффициента b[k]
    g1 = graph[0][485:530]
    for per in range(len(g1)):
        if t < np.pi:
            y = g1[per] * np.sin(omega * k * t)
        else:
            y = -g1[per] * np.sin(omega * k * t)
    return y


kef_a = [round(2*quad(func_1, -2e5, 2e5, args=(k, freq))[0]/T, 3) for k in m]  # интеграл для a[k], k -номер гармоники
kef_b = [round(2*quad(func_2, -2e5, 1e5, args=(k, freq))[0]/T, 3) for k in m]  # интеграл для b[k], k -номер гармоники

A = np.array([((kef_a[k]**2+kef_b[k]**2)**0.5)/100 for k in m])  # численные значения амплитуды гармоник
A[3] = A[3]/10

# plt.plot([m[1], m[1]], [0, A[1]], label='1 гармоника')
# plt.plot([m[2], m[2]], [0, A[2]], label='2 гармоника')
# plt.plot([m[3], m[3]], [0, A[3]], label='3 гармоника')

# plt.show()
