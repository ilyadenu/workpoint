import matplotlib.pyplot as plt
import numpy as np
from archive.stat import Uf_approx_sinus_stat
from filtration import FourierFilter
from phase import PhaseCalculation


class Main(FourierFilter, PhaseCalculation):

    def __init__(self, first_file: int, last_file: int):
        PhaseCalculation.__init__(self, first_file, last_file)
        FourierFilter.__init__(self)

    def init_cond_plots(self, figure: int):

        plt.figure()
        plt.grid(True)
        self.export_from_excel()
        self.find_max_position_x()
        self.find_min_position_x()
        self.find_max_x()
        self.find_min_x()
        self.u_params_calc()

        if figure == 1:

            plt.title('Начальные условия')
            plt.ylabel('Uфп, В')
            plt.xlabel('Время, с')

            graph_up = [i * 250 for i in self.graph[self.first_file]]
            plt.plot(self.osc_time,
                     graph_up,
                     label='Uфп * 250')  # исходный график сигнала фотоприемника
            plt.plot(self.osc_time, self.graph_saw[self.first_file], label='Uп')  # исходный график пилы
            plt.legend()

        elif figure == 2:

            plt.title('Зависимость Uфп от Uп')
            plt.ylabel('Uфп, В')
            plt.xlabel('Uп, В')

            plt.plot(self.graph_saw[self.first_file][495:530],
                     self.graph[self.first_file][495:530])  # зависимость сигнала фотоприемника от пилы
            plt.plot(self.time,
                     self.uf_approx_sinus)  # зависимость аппроксимированного сигнала фотоприемника от времени синусоиды

        else:

            plt.title('Стандарт частоты')
            plt.ylabel('Uсч, В')
            plt.xlabel('Время, с')

            plt.plot(self.time, self.u())  # зависимость синусоиды от времени

        plt.show()

    def approximation_plots(self, figure: int):

        plt.figure()
        plt.grid(True)
        self.export_from_excel()
        self.g_gs_approx()
        self.maximum_matching()

        if figure == 1:

            plt.title('Аппроксимирование зависимости Uфп от Uп')
            plt.ylabel('Uфп, В')
            plt.xlabel('Uп, В')

            plt.scatter(self.graph_saw[self.first_file][495:530],
                        self.graph[self.first_file][495:530],
                        label='Зависимость Uфп от Uп')  # точки зависимости сигнала от пилы
            plt.plot(self.saw_approx, self.uf_approx, color="r",
                     label='Аппроксимация логарифмом')  # аппроксимация зависимости сигнала от пилы
            plt.legend()

        else:

            plt.title('Сигнал стандарта частоты после модулятора')
            plt.ylabel('Uфп, В')
            plt.xlabel('Время, с')

            plt.plot(self.time[470:520],
                     self.uf_approx_sinus[470:520])  # зависимость аппроксимированного сигнала фотоприемника от
            # времени синусоиды
            plt.plot(self.time[470:520],
                     Uf_approx_sinus_stat[470:520])

            print(self.phase)

        plt.show()

    def filtration_plots(self, figure: int):

        plt.figure()
        plt.grid(True)
        self.frequency()
        self.fft_for_signal()
        self.harmonics_calc()

        if figure == 1:

            plt.title('Гармоники')
            plt.ylabel('Амплитуда')
            plt.xlabel('Частота, Гц')

            plt.plot(self.freq, np.abs(self.direct_trans_with_harms))

        else:

            plt.title('Очищенный сигнал')
            plt.ylabel('Uфп, В')
            plt.xlabel('Время, с')

            plt.plot(self.fft_time, self.inverse_trans)

        plt.show()


if __name__ == '__main__':
    main = Main(17, 18)
    # main.init_cond_plots(3)
    main.approximation_plots(2)
    # main.filtration_plots(2)
