import numpy as np
import cmath as cm
from scipy.integrate import quad
from approximation import Uf_approx_sinus
from freq import frequency
from main import time

fourier_transform = []  # Список значений преобразований Фурье


def fourier_func(t, u: list[float], freq_for_func: float) -> list[float]:
    j = cm.sqrt(-1)
    return u*np.exp(-j*freq_for_func*t)


freq = [(2*np.pi)/i for i in time]
freq[17] = 10**-10

f1 = [[uf, frequency, quad(fourier_func, -np.inf, np.inf, args=(uf, frequency))[0]] for uf in Uf_approx_sinus]

for i in range(len(f1)):
    fourier_transform.append(f1[i][2])
