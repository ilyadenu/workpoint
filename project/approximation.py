import numpy as np
from scipy.optimize import curve_fit

from archive.stat import Uf_approx_sinus_stat
from sinus_definition import InitialConditions, init_sinus


def parabolic_f(x: float, a: float, b: float, c: float) -> float:

    """Функция для аппроксимации параболой"""

    return -a * (x ** 2 + b) + c


def logarithmic_f(x: float, a: float, b: float, c: float) -> list[float]:

    """Функция для аппроксимации логарифмом"""

    return a * np.log2(x - b) - c


class Approximation(InitialConditions):

    def __init__(self, first_file: int, last_file: int):
        super().__init__(first_file, last_file)
        self.saw_approx = []
        self.uf_approx_sinus = None
        self.uf_approx = None

    def g_gs_approx(self) -> tuple[list[float], list[float]]:

        """ Функция для аналитического представления зависимости сигнала пилообразного напряжения от
            сигнала фотоприемника. А так же для моделирования "прохождения" синусоидального сигнала
            через электрооптический модулятор"""

        popt = curve_fit(logarithmic_f,
                         self.graph_saw[self.first_file][495:530],
                         self.graph[self.first_file][495:530],
                         p0=[1000, -100, -0.00001])

        a_opt, b_opt, c_opt = popt[0]
        self.saw_approx = np.linspace(min(self.graph_saw[self.first_file][495:530]),
                                      max(self.graph_saw[self.first_file][495:530]),
                                      1000)

        self.uf_approx = logarithmic_f(self.saw_approx,
                                       a_opt,
                                       b_opt,
                                       c_opt)  # аппроксимация зависимости сигнала от пилы

        self.uf_approx_sinus = logarithmic_f(init_sinus,
                                             a_opt,
                                             b_opt,
                                             c_opt)  # аппроксимация выходного сигнала

        return self.uf_approx, self.uf_approx_sinus


approximation = Approximation(17, 18)
approximation.export_from_excel()
approximation.g_gs_approx()
Uf_approx_sinus = approximation.uf_approx_sinus

uf = Uf_approx_sinus[470:520]
uf_1 = Uf_approx_sinus_stat[470:520]

count = 0
for i in range(len(uf)):
    count += 1
    if uf[i] == max(uf):
        print(1)

print(count)

count_1 = 0
for i in range(len(uf_1)):
    count_1 += 1
    if uf[i] == max(uf_1):
        print(1)

print(count_1)
