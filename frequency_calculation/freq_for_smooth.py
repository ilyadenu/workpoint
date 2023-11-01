import numpy as np
from approximation import uf_func
from max_min_find import max_min_find

Uf = uf_func(7, 8)[0]
time_for_sin = np.linspace(-5*10e-7, 5*10e-7, 870)
maximal = max_min_find(Uf)[0][1:]
minimal = max_min_find(Uf)[1]


def frequency_calculation(time_for_func, maximal, minimal, uf) -> float:
    time_min = []
    time_max = []
    period_max = []
    period_min = []

    for ii in range(len(maximal)):
        for i in range(len(time_for_func)):
            if uf[i] == maximal[ii]:
                time_max.append(time_for_func[i])

    for jj in range(len(minimal)):
        for j in range(len(time_for_func)):
            if uf[j] < minimal[jj]:
                time_min.append(time_for_func[j])

    for g in range(0, 1):
        time_max_calc = abs(time_max[g] - time_max[g+1])
        period_max.append(time_max_calc)

    for h in range(0, 2):
        time_min_calc = abs(time_min[h] - time_min[h+1])
        period_min.append(time_min_calc)

    period_max_aver = sum(period_max)/1
    period_min_aver = sum(period_min)/2
    period_fin = (period_max_aver+period_min_aver)/2

    func_frequency = (2*np.pi)/period_fin

    return func_frequency


frequency_for_smooth = frequency_calculation(time_for_sin, maximal, minimal, Uf)
# print(frequency_for_smooth)

