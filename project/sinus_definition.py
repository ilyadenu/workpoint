import os
import numpy as np
import pandas as pd


class InitialConditions:

    def __init__(self, first_file: int, last_file: int):
        self.omega = 1e7
        self.time = np.linspace(-5 * 10e-7, 5 * 10e-7, 1000)
        self.first_file = first_file
        self.last_file = last_file
        self.osc_time = []  # Время взятое с осциллографа
        self.graph_saw = []  # Сигнал пилообразного напряжения (значения из экселя)
        self.graph = []  # Сигнал фотоприемника (значения из экселя)
        self.path_list = []  # Список с файлами формата csv
        self.find_position_max = []  # Индексы максимумов из списка graph
        self.find_position_min = []  # Индексы минимумов из списка graph
        self.average_max_x = []  # Максимумы по оси абцисс
        self.average_min_x = []  # Минимумы по оси абцисс
        self.u0 = 0  # Параметры синусоиды
        self.um = 0  # Параметры синусоиды

    def export_from_excel(self):

        directory = 'measurements'

        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                if 'csv' in f:
                    self.path_list.append(f)

        for file_change in self.path_list:
            df = pd.read_csv(file_change)
            origin = df['3'].to_list()
            saw = df['2'].to_list()
            self.osc_time = df['1'].to_list()
            self.graph.append(origin)
            self.graph_saw.append(saw)

    def find_max_position_x(self):

        """Функция поиска номера максимума в списке graph"""

        piece_of_res = []

        for i in range(self.first_file, self.last_file):

            piece_of_res.append(self.graph[i][485:530])
            piece_of_res_0 = piece_of_res[0]
            peak = max(self.graph[i][485:530])

            for j in range(len(piece_of_res_0)):
                if piece_of_res_0[j] == peak:
                    self.find_position_max.append(485 + j)

        return self.find_position_max

    def find_min_position_x(self):

        """Функция поиска номера минимума в списке graph"""

        piece_of_res = []

        for g in range(self.first_file, self.last_file):

            piece_of_res.append(self.graph[g][440:480])
            piece_of_res_0 = piece_of_res[0]
            peak = min(self.graph[g][440:480])

            for i in range(len(piece_of_res_0)):
                if piece_of_res_0[i] == peak:
                    self.find_position_min.append(440 + i)

        return self.find_position_min

    def find_max_x(self):

        """Функция нахождения значения максимума по оси x"""

        value_origin = []

        for i in range(len(self.find_position_max)):
            unit = self.find_position_max[i]
            value_origin.append(self.graph_saw[0][unit])
        del self.find_position_max[0:len(self.find_position_max)]
        average = sum(value_origin) / len(value_origin)

        return self.average_max_x.append(average)

    def find_min_x(self):

        """Функция нахождения значения минимума по оси x"""

        value_origin = []

        for i in range(len(self.find_position_min)):
            unit = self.find_position_min[i]
            value_origin.append(self.graph_saw[0][unit])
        del self.find_position_min[0:len(self.find_position_min)]
        average = sum(value_origin) / len(value_origin)

        return self.average_min_x.append(average)

    def u_params_calc(self):

        """Функция расчета параметров синусоиды"""

        self.u0 = (self.average_max_x[0] + self.average_min_x[0]) / 3
        self.um = (self.average_max_x[0] - self.u0) / 1

        return self.u0, self.um

    def u(self):

        """Функция синусоидального сигнала, который подается на рабочую точку"""

        return self.u0 + self.um * np.sin(self.omega * self.time)

    def func_for_start(self):
        self.export_from_excel()
        self.find_max_position_x()
        self.find_min_position_x()
        self.find_max_x()
        self.find_min_x()
        self.u_params_calc()


measurement = InitialConditions(17, 18)
measurement.func_for_start()
init_sinus = measurement.u()

