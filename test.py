import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from fourier.fourier_fft import cut_clear_sig

# Заданные данные
x = np.array(range(len(cut_clear_sig)))
y = np.array([-0.03621736+0.j, 0.03621736+0.j, -0.03621736+0.j, 0.03621736+0.j,
              -0.03621736+0.j, 0.03621736+0.j, -0.03621736+0.j, 0.03621736+0.j,
              -0.03621736+0.j, 0.03621736+0.j, -0.03621736+0.j, 0.03621736+0.j,
              -0.03621736+0.j, 0.03621736+0.j, -0.03621736+0.j, 0.03621736+0.j,
              -0.03621736+0.j, 0.03621736+0.j, -0.03621736+0.j, 0.03621736+0.j,
              -0.03621736+0.j, 0.03621736+0.j, -0.03621736+0.j, 0.03621736+0.j,
              -0.03621736+0.j, 0.03621736+0.j, -0.03621736+0.j, 0.03621736+0.j,
              -0.03621736+0.j, 0.03621736+0.j])

# Определение функции, которую будем аппроксимировать
def func(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

# Аппроксимация с помощью `curve_fit`
params, params_covariance = curve_fit(func, x, y)

# Распаковка параметров аппроксимации
a, b, c, d = params

# Генерация значений для плавной кривой аппроксимации
x_smooth = np.linspace(0, len(cut_clear_sig)-1, 1000)
y_smooth = func(x_smooth, a, b, c, d)

# Отображение результатов
plt.scatter(x, y, label='Исходные данные')
plt.plot(x_smooth, y_smooth, label='Аппроксимация')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Аппроксимация функции')
plt.legend()
plt.show()
