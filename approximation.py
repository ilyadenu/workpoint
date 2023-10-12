import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sinus_calc import u, graph_saw, graph
from sinus_calc import u_params_calc

path, dirs, files = next(os.walk("/home/admin/Work/50_измерений"))
file_count = len(files)


def logarithmic_f(x, a, b, c):  # функция для аппроксимации логарифмом
    return a*np.log2(x-b) - c


# def parabolic_f(x,a,b,c): # функция для аппроксимации параболой
#     return -a*(x**2 + b) + c


def sin_f(x, a, b, c, d):  # функция для аппроксимации синусоидой
    return 5*a*np.sin(b * x + c) + d


gs = graph_saw[0][495:530]  # массив значений пилы
g = graph[0][495:530]  # массив значений сигнала
# U0 = u_params_calc(7, 8)[0]
# Um = u_params_calc(7, 8)[1]
# sinus = u(U0, Um)  # вычисленный синус
# sinus2 = u(U0, Um)[365:400]  # кусок синуса для выходного сигнала
time = np.linspace(-5*10e-7, 5*10e-7, 35)  # время для куска синуса
time_for_sin = np.linspace(-5*10e-7, 5*10e-7, 1000)  # время для аппроксимированного синуса


def g_gs_approx(l_border: int, r_border: int) -> tuple:


    popt, pcov = curve_fit(logarithmic_f, gs, g, p0=[1000, -1000, -0.000001])

    a_opt, b_opt, c_opt = popt

    u0 = u_params_calc(l_border, r_border)[0]
    um = u_params_calc(l_border, r_border)[1]
    sinus = u(u0, um)  # вычисленный синус
    sinus2 = u(u0, um)[365:400]  # кусок синуса для выходного сигнала

    saw_approx = np.linspace(min(gs), max(gs), 35)  # массив точек для аппроксимации
    uf_approx = logarithmic_f(saw_approx, a_opt, b_opt, c_opt)  # аппроксимация зависимости сигнала от пилы
    uf_approx_sinus = logarithmic_f(sinus2, a_opt, b_opt, c_opt)  # аппроксимация выходного сигнала

    return uf_approx, uf_approx_sinus


def uf_func(l_border: int, r_border: int) -> tuple:

    uf_approx = g_gs_approx(l_border, r_border)[0]
    uf_approx_sinus = g_gs_approx(l_border, r_border)[1]

    x_value = np.array([i for i in range(len(uf_approx_sinus))])  # массив точек для аппроксимации

    params, params_covariance = curve_fit(sin_f, x_value, uf_approx_sinus)

    a, b, c, d = params

    x_smooth = np.linspace(0, len(uf_approx_sinus) - 1, 1000)  # массив точек для гладкой аппроксимации
    uf = sin_f(x_smooth, a, b, c, d)  # гладкая аппроксимация выходного сигнала

    for i in range(len(uf)):
        uf[i] = uf[i]*0.98

    return uf, c


# Uf = uf_func(0, 1)[0]

# plt.ylabel('Выходной сигнал, В')
# plt.xlabel('Время, с')
# plt.grid(True)
# plt.scatter(gs, g)  # точки зависимости сигнала от пилы
# plt.plot(saw_approx, Uf_approx, color="r")  # аппроксимация зависимости сигнала от пилы
# plt.plot(time, Uf_approx_sinus) # зависимость аппроксимированного сигнала фотоприемника от времени синусоиды
# plt.plot(time_for_sin, u(U0, Um)[69:939])  # выходной сигнал
# plt.plot(time_for_sin, Uf)  # гладкий выходной сигнал
# plt.show()
