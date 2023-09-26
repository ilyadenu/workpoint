import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

from main import u
from position_find import graph_saw, graph, U0, Um


def model_f(x, a, b, c):  # функция для аппроксимации логарифмом
    return -a*np.log2(x-b) - c


# def model_f(x,a,b,c): # функция для аппроксимации параболой
#     return -a*(x**2 + b) + c


def model_sin(x, a, b, c):
    return a + b * np.sin(x + c)


gs = graph_saw[0][495:530]
g = graph[0][495:530]
sinus = u(U0, Um)
sinus2 = u(U0, Um)[365:400]
time = np.linspace(-5*10e-7, 5*10e-7, 35)
time_for_sin = np.linspace(-5*10e-7, 5*10e-7, 870)

popt, pcov = curve_fit(model_f, gs, g, p0=[2.8, -7.3, -1.86e-05])

a_opt, b_opt, c_opt = popt

saw_approx = np.linspace(min(gs), max(gs), 35)
Uf_approx = model_f(saw_approx, a_opt, b_opt, c_opt)
Uf_approx_sinus = model_f(sinus2, a_opt, b_opt, c_opt)

sin_x = np.array([i for i in range(len(Uf_approx_sinus))])
sin_y = np.array(Uf_approx_sinus)

# for i in range(len(graph[0])):
#     graph[0][i] = graph[0][i]*150

# Проведем полиномиальную интерполяцию
coefficients = np.polyfit(sin_x, sin_y, deg=30)
p = np.poly1d(coefficients)

# Зададим точки для плавной кривой приближения
x_smooth = np.linspace(0, len(Uf_approx_sinus) - 1, 1000)
y_smooth = p(x_smooth)

Uf = y_smooth[69:939]  # выходной сигнал после модулятора
x_smooth = x_smooth[69:939]


# plt.ylabel('Выходной сигнал, В')
# plt.xlabel('Время, с')
# plt.grid(True)
# plt.scatter(gs, g, label="Полученная зависимость")
# plt.plot(saw_approx, Uf_approx, color="r", label="Аппроксимация")
# plt.plot(time, Uf_approx_sinus) # зависимость аппроксимированного сигнала фотоприемника от времени синусоиды
# plt.plot(time_for_sin, u(U0, Um)[69:939])
# plt.plot(time_for_sin, Uf)
# plt.show()
