import numpy as np
from approximation import Uf

time_for_sin = np.linspace(-5*10e-7, 5*10e-7, 870)


def frequency_calculation(time_for_func: list[int], uf: list[int]) -> float:
    time_max = []
    time_min = []
    period_max = []
    period_min = []

    for i in range(len(time_for_func)):
        if uf[i] > -6.9:
            time_max.append(time_for_func[i])

    for j in range(len(time_for_func)):
        if uf[j] < -9.7:
            time_min.append(time_for_func[j])

    for g in range(0, 110):
        time_max_calc = abs(time_max[g] - time_max[g+1])
        period_max.append(time_max_calc)

    for h in range(0, 110):
        time_min_calc = abs(time_min[h] - time_min[h+1])
        period_min.append(time_min_calc)

    period_max_aver = sum(period_max)/111
    period_min_aver = sum(period_min)/111
    period_fin = (period_max_aver+period_min_aver)/2

    func_frequency = (2*np.pi)/period_fin

    return func_frequency


frequency = frequency_calculation(time_for_sin, Uf)

# print(frequency)
