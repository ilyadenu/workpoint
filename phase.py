from approximation import Uf_approx_sinus
from main import time


def phase_calculation(time_for_func: list[int], uf: list[int], clear_sig: list[int]) -> int:
    time_max_u = 0
    time_max_clear = 0

    for i in range(len(time_for_func)):
        if uf[i] > -6.9:
            time_max_u = time_for_func[i]

    for j in range(len(time_for_func)):
        if clear_sig[j] == max(clear_sig):
            time_max_clear = time_for_func[j]

    time_offset = time_max_u - time_max_clear

    return time_offset


time_calc = time[10:16]
Uf_approx_sinus_calc = Uf_approx_sinus[10:16]

phase = phase_calculation(time_calc, Uf_approx_sinus_calc, clear_sig)

# print(phase)
