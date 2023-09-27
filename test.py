import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

from approximation import Uf_approx_sinus

# Заданные данные
x = np.array([i for i in range(len(Uf_approx_sinus))])


# Определение функции, которую будем аппроксимировать
def func(x, a, b, c, d):
    return 5*a * np.sin(b * x + c) + d

# Аппроксимация с помощью curve_fit
params, params_covariance = curve_fit(func, x, Uf_approx_sinus)

# Распаковка параметров аппроксимации
a, b, c, d = params

# Генерация значений для плавной кривой аппроксимации
x_smooth = np.linspace(0, len(Uf_approx_sinus) - 1, 1000)
y_smooth = func(x_smooth, a, b, c, d)
print(c)
# 3.3736216659714406
for i in range(len(y_smooth)):
    y_smooth[i] = y_smooth[i]*0.98

# Отображение результатов
plt.scatter(x, Uf_approx_sinus, label='Исходные данные')
plt.plot(x_smooth, y_smooth, label='Аппроксимация')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Аппроксимация функции')
plt.legend()
plt.show()
