# Блок импортов
import numpy as np
from matplotlib import pyplot as plt
from approximation import Uf_approx_sinus
from position_find import graph, osc_time, graph_saw, U0, Um

time = np.linspace(-5*10e-7, 5*10e-7, 35)


def u(u0, um):  # Функция синусоидального сигнала, который подается на рабочую точку
    f = 1e7
    omega = 2 * np.pi * f
    t = np.linspace(-5*10e-7, 5*10e-7, 1000)
    return u0 + um*np.sin(omega*t)


# plt.plot(osc_time, graph[0])  # исходный график сигнала
# plt.plot(osc_time, graph_saw[0])  # исходный график пилы
# plt.plot(graph_saw[0][495:530], graph[0][495:530])  # зависимость сигнала фотоприемника от пилы
# plt.plot(np.linspace(-5*10e-7, 5*10e-7, 45), u(U0, Um)[485:530])  # зависимость синусоиды от времени
# plt.plot(graph[0][485:530], u(U0, Um)[485:530])  # зависимость аппроксимированного сигнала фотоприемника от синусоиды
# plt.plot(time, Uf_approx_sinus)  # зависимость аппроксимированного сигнала фотоприемника от времени синусоиды
# plt.show()
