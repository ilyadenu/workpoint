import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from main import u, graph_saw, graph, left, right
from main import u_params_calc


def logarithmic_f(x, a, b, c):  # функция для аппроксимации логарифмом
    return a * np.log2(x - b) - c


# def parabolic_f(x,a,b,c): # функция для аппроксимации параболой
#     return -a*(x**2 + b) + c


def sin_f(x, a, b, c, d):  # функция для аппроксимации синусоидой
    return 5 * a * np.sin(b * x + c) + d


gs = graph_saw[left][495:530]  # массив значений пилы
g = graph[left][495:530]  # массив значений сигнала
saw_approx = np.linspace(min(gs), max(gs), 1000)
time_for_sin = np.linspace(-5 * 10e-7, 5 * 10e-7, 1000)  # время для аппроксимированного синуса


def g_gs_approx(l_border: int, r_border: int) -> tuple:

    popt, pcov = curve_fit(logarithmic_f, gs, g, p0=[1000, -100, -0.00001])

    a_opt, b_opt, c_opt = popt

    u0 = u_params_calc(l_border, r_border)[0]
    um = u_params_calc(l_border, r_border)[1]
    sinus = u(u0, um)  # вычисленный синус

    uf_approx = logarithmic_f(saw_approx, a_opt, b_opt, c_opt)  # аппроксимация зависимости сигнала от пилы
    uf_approx_sinus = logarithmic_f(sinus, a_opt, b_opt, c_opt)  # аппроксимация выходного сигнала

    return uf_approx, uf_approx_sinus, sinus


# def uf_func(l_border: int, r_border: int) -> tuple:
#
#     uf_approx_sinus = g_gs_approx(l_border, r_border)[1]
#
#     x_value = np.array([i for i in range(len(uf_approx_sinus))])  # массив точек для аппроксимации
#
#     params, params_covariance = curve_fit(sin_f, x_value, uf_approx_sinus)
#
#     a, b, c, d = params
#
#     x_smooth = np.linspace(0, len(uf_approx_sinus) - 1, 1000)  # массив точек для гладкой аппроксимации
#     uf = sin_f(x_smooth, a, b, c, d)  # гладкая аппроксимация выходного сигнала
#
#     # for i in range(len(uf)):
#     #     uf[i] = uf[i] * 0.98
#
#     return uf, c


Uf_approx = g_gs_approx(left, right)[0]
Uf_approx_sinus = g_gs_approx(left, right)[1]
U_signal = g_gs_approx(left, right)[2]


# plt.figure()
# plt.title('Сигнал стандарта частоты после модулятора')
# plt.ylabel('Uфп, В')
# plt.xlabel('Время, с')
# plt.grid(True)
# plt.scatter(gs, g, label='Зависимость Uфп от Uп')  # точки зависимости сигнала от пилы
# plt.plot(saw_approx, Uf_approx, color="r",
#          label='Аппроксимация логарифмом')  # аппроксимация зависимости сигнала от пилы
# plt.plot(time_for_sin, Uf_approx_sinus)  # зависимость аппроксимированного сигнала фотоприемника от времени синусоиды
# plt.plot(time_for_sin, U_signal)  # выходной сигнал
# plt.legend()
# plt.show()
