import numpy as np
from approximation import Uf_approx_sinus

time_for_sin = np.linspace(-5*10e-7, 5*10e-7, 1000)


def freq(uf_appr: list[float]) -> float:

    min_list = []
    max_list = []
    time_min = []
    time_max = []
    period_min = []
    period_max = []

    count = uf_appr[0]

    for i in range(1, len(uf_appr)):

        if count > uf_appr[i]:
            count = uf_appr[i]

        elif uf_appr[i-2] > count < uf_appr[i+2]:
            min_list.append(count)
            time_min.append(time_for_sin[i])

        elif count < uf_appr[i+1]:
            count = uf_appr[i+1]

        else:
            max_list.append(count)
            time_max.append(time_for_sin[i])

    for g in range(len(time_max) - 1):
        time_max_calc = abs(time_max[g] - time_max[g + 1])
        period_max.append(time_max_calc)

    for h in range(len(time_min) - 1):
        time_min_calc = abs(time_min[h] - time_min[h + 1])
        period_min.append(time_min_calc)

    period_max_aver = sum(period_max) / len(period_max)
    period_min_aver = sum(period_min) / len(period_min)
    period_fin = (period_max_aver + period_min_aver) / 2

    func_frequency = (2 * np.pi) / period_fin

    return func_frequency


freq = freq(Uf_approx_sinus)

