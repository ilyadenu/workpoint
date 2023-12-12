import numpy as np

from archive.approximation_old import Uf


def fourier_trans(data, k: int) -> tuple:
    re = 0
    im = 0
    num = len(data)
    for n in range(num):
        a1, b1 = data[n]
        arg = 2 * np.pi * k * n / num
        a2 = np.cos(arg)
        b2 = np.sin(arg)
        re += (a1 * a2 - b1 * b2)
        im -= (a1 * b2 + a2 * b1)

    return re, im


def inv_fourier_trans(data, n: int) -> tuple:
    re = 0
    im = 0
    num = len(data)
    for k in range(num):
        a1, b1 = data[k]
        arg = 2 * np.pi * k * n / num
        a2 = np.cos(arg)
        b2 = np.sin(arg)
        re += (a1 * a2 - b1 * b2)
        im -= (a1 * b2 + a2 * b1)

    return re / num, im / num


def fourier_trans_real(data, k: int) -> tuple:
    re = 0
    im = 0
    num = len(data)
    for n in range(num):
        x = data[n]
        arg = 2 * np.pi * k * n / num
        re += x * np.cos(arg)
        im -= x * np.sin(arg)

    return re, im


r = 870
num = range(r)

spectrum = []
for k in num:
    re, im = fourier_trans_real(Uf, k)
    spectrum.append((re, im))

Uf_inv = []
for n in num:
    re, im = inv_fourier_trans(spectrum, n)
    Uf_inv.append((re, im))

Uf_inv_im = []
Uf_inv_re = []
for j in range(len(Uf_inv)):
    Uf_inv_im.append(Uf_inv[j][1])
    Uf_inv_re.append(Uf_inv[j][0])

for i in range(len(Uf_inv_re)):
    if Uf_inv_re[i] == max(Uf_inv_re):
        print(i)

for i in range(len(Uf)):
    if Uf[i] == max(Uf):
        print(i)

# plt.plot(time_for_sin, Uf)
# plt.plot(time_for_sin, Uf_inv_re)
# plt.grid(True)
# plt.show()
