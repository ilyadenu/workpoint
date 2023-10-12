import numpy as np
from scipy.optimize import curve_fit

from approximation import uf_func
from sinus_calc import find_max_x, find_min_x, u_params_calc
import matplotlib.pyplot as plt

phase_list = [2.0566935545441294, 2.059077016866184, 2.0201007875274044, 1.959933418576996, 2.059077016866184,
              2.059077016866184, 2.059077016866184, 2.0020372204524324, 2.0566935545441294, 2.0566935545441294,
              2.059077016866184, 2.059077016866184, 2.059077016866184, 2.01152629913649, 1.9869177809956848,
              2.0566935545441294, 2.059077016866184, 2.059077016866184, 2.059077016866184]
x = np.arange(0, 19, 1)


def parabolic_f(x,a,b,c):  # функция для аппроксимации параболой
    return -a*(x**2 + b) + c


def phase_clac() -> float:

    for num in range(18, 19):

        find_max_x(num, num + 1)
        find_min_x(num, num + 1)
        u_params_calc(num, num + 1)
        phase = uf_func(num, num + 1)[1]
        print(phase)

    return phase


phase_clac()

popt, pcov = curve_fit(parabolic_f, x, phase_list, p0=[3, 1.95, 0.001])

a_opt, b_opt, c_opt = popt

x_approx = np.linspace(min(x), max(x), 19)  # массив точек для аппроксимации
phase_approx = parabolic_f(x_approx, a_opt, b_opt, c_opt)  # аппроксимация зависимости сигнала от пилы

plt.figure('Изменение фазы')
plt.xlabel('Количество измерений')
plt.ylabel('Фаза')
plt.grid(True)
plt.scatter(x, phase_list)
plt.plot(x_approx, phase_approx, color='red')
plt.show()
