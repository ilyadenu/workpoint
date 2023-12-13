import numpy as np
from numpy.fft import fft, fftfreq, ifft
from approximation import Uf_approx_sinus


class FourierFilter:

    def __init__(self):
        self.freq_time = np.linspace(-5 * 10e-7, 5 * 10e-7, 1000)
        self.fft_time = np.linspace(-8.1*10e-8, 8.1*10e-8, 1000)
        self.dot_value = 1000
        self.func_frequency = None
        self.freq = []
        self.direct_trans_with_harms = []
        self.direct_trans = []
        self.inverse_trans = []
        self.harm_rel = []

    def frequency(self) -> float:

        """Функция для расчета частоты сигнала прошедшего через электрооптический модулятор
            Сигнал на вид похож на синусоиду, но это не совсем так, из-за его негармоничности
            Поэтому необходимо сначала найти все минимумы и максимумы, а уже затем считать частоту"""

        min_list = []
        max_list = []
        time_min = []
        time_max = []
        period_min = []
        period_max = []

        count = Uf_approx_sinus[0]

        for i in range(1, len(Uf_approx_sinus)):

            if count > Uf_approx_sinus[i]:
                count = Uf_approx_sinus[i]

            elif Uf_approx_sinus[i - 2] > count < Uf_approx_sinus[i + 2]:
                min_list.append(count)
                time_min.append(self.freq_time[i])

            elif count < Uf_approx_sinus[i + 1]:
                count = Uf_approx_sinus[i + 1]

            else:
                max_list.append(count)
                time_max.append(self.freq_time[i])

        for g in range(len(time_max) - 1):
            time_max_calc = abs(time_max[g] - time_max[g + 1])
            period_max.append(time_max_calc)

        for h in range(len(time_min) - 1):
            time_min_calc = abs(time_min[h] - time_min[h + 1])
            period_min.append(time_min_calc)

        period_max_aver = sum(period_max) / len(period_max)
        period_min_aver = sum(period_min) / len(period_min)
        period_fin = (period_max_aver + period_min_aver) / 2

        self.func_frequency = (2 * np.pi) / period_fin

        return self.func_frequency

    def fft_for_signal(self) -> tuple:

        """Функция переводит сигнал из временной области в частотную.
            Обрезает все гармоники оставляя чистый сигнал.
            Затем происходит перевод из частотной области во временную.
            На выходе получается очищенный от гармоник сигнал."""

        self.direct_trans_with_harms = fft(Uf_approx_sinus)

        freq = fftfreq(self.dot_value, 1 / self.func_frequency)
        self.freq = [i + 1 * 10e6 for i in freq]

        shift = 16

        self.direct_trans = np.roll(self.direct_trans_with_harms, shift)

        self.direct_trans[:shift] = 0
        self.direct_trans[shift + 1:] = 0

        self.inverse_trans = ifft(self.direct_trans)

        return self.direct_trans, self.freq, self.inverse_trans

    def harmonics_calc(self) -> list:

        """Функция для расчета гармоник сигнала"""

        harmonics_list = [h for h in np.abs(self.direct_trans_with_harms) if h > 0.22]
        harmonics_list.sort(reverse=True)
        self.harm_rel.append(harmonics_list[0])
        j = 0

        for i in range(len(harmonics_list) - 3):
            avg = (harmonics_list[i + j + 1] + harmonics_list[i + j + 2]) / 2
            self.harm_rel.append(avg)
            j += 1

        return self.harm_rel

    def prints_harmonics(self):

        h2_h1_rel = self.harm_rel[1] / self.harm_rel[0]
        h3_h2_rel = self.harm_rel[2] / self.harm_rel[1]
        h3_h1_rel = self.harm_rel[2] / self.harm_rel[0]

        print('Отношение 2 гармоники к 1 = ', h2_h1_rel, '\n',
              'Отношение 3 гармоники к 2 = ', h3_h2_rel, '\n',
              'Отношение 3 гармоники к 1 = ', h3_h1_rel)


filter_ = FourierFilter()
filter_.frequency()
filter_.fft_for_signal()
filter_.harmonics_calc()

