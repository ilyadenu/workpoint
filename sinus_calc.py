import numpy as np
import pandas as pd
import os


path_list = []  # Список для хранения там пути к csv файлам
graph = []  # Список значений измерения
graph_b = []  # Список значений времени осциллографа
graph_saw = []  # Список значений пилы
min_list = []  # Список минимальных значений измерения
max_list = []  # Список максимальных значений измерения
find_position_max = []  # Список номеров максимальных значений по оси x в списке graph
find_position_min = []  # Список номеров минимальных значений по оси x в списке graph
average_max_x = []  # Список средних значений максимумов, посчитанный из find_position_max
average_min_x = []  # Список средних значений минимумов, посчитанный из find_position_min


def u(u0, um):  # Функция синусоидального сигнала, который подается на рабочую точку
    f = 1e7
    omega = 2 * np.pi * f
    t = np.linspace(-5*10e-7, 5*10e-7, 1000)
    return u0 + um*np.sin(omega*t)


def find_max_position_x(left_border: int, right_border: int):  # Функция поиска номера максимума в списке graph
    a = []
    for g in range(left_border, right_border):
        a.append(graph[g][485:530])
        a1 = a[0]
        b = max(graph[g][485:530])
        for i in range(len(a1)):
            if a1[i] == b:
                find_position_max.append(485 + i)


def find_min_position_x(left_border: int, right_border: int):  # Функция поиска номера минимума в списке graph
    a = []
    for g in range(left_border, right_border):
        a.append(graph[g][440:480])
        a1 = a[0]
        b = min(graph[g][440:480])
        for i in range(len(a1)):
            if a1[i] == b:
                find_position_min.append(440 + i)


def find_max_x(l_border: int, r_border: int):  # Функция нахождения значения максимума по оси x
    find_max_position_x(l_border, r_border)
    value_origin = []
    for i in range(len(find_position_max)):
        unit = find_position_max[i]
        value_origin.append(graph_saw[0][unit])
    del find_position_max[0:len(find_position_max)]
    average = sum(value_origin) / len(value_origin)
    average_max_x.append(average)


def find_min_x(l_border: int, r_border: int):  # Функция нахождения значения минимума по оси x
    find_min_position_x(l_border, r_border)
    value_origin = []
    for i in range(len(find_position_min)):
        unit = find_position_min[i]
        value_origin.append(graph_saw[0][unit])
    del find_position_min[0:len(find_position_min)]
    average = sum(value_origin) / len(value_origin)
    average_min_x.append(average)


directory = '/home/admin/Work/50_измерений'
# directory = '/home/ilya/Desktop/50 измерений'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        if 'csv' in f:
            path_list.append(f)

for file_change in path_list:
    df = pd.read_csv(file_change)
    origin = df['3'].to_list()
    saw = df['2'].to_list()
    osc_time = df['1'].to_list()
    graph.append(origin)
    graph_saw.append(saw)
    min_list.append(min(origin[440:480]))
    max_list.append(max(origin[485:530]))


def u_params_calc(l_border: int, r_border: int):

    find_max_x(l_border, r_border)
    find_min_x(l_border, r_border)

    u0 = (average_max_x[0]+average_min_x[0])/3
    um = (average_max_x[0]-u0)/1

    return u0, um

# # print("Значение параметра U0 =", U0, "\n", "Значение параметра Um =", Um)
#
# # plt.plot(osc_time, graph[0])  # исходный график сигнала
# # plt.plot(osc_time, graph_saw[0])  # исходный график пилы
# # plt.plot(graph_saw[0][495:530], graph[0][495:530])  # зависимость сигнала фотоприемника от пилы
# # plt.plot(np.linspace(-5*10e-7, 5*10e-7, 45), u(U0, Um)[485:530])  # зависимость синусоиды от времени
# # plt.show()

