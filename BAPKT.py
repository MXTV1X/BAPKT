import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import constants

# данные Кербина
m0 = 41904
M = m0 + 36482  # масса с топливом
Ft = 3268861.02  # тк сами рассчитать не смогли, взяли среднее из интернета
Cf = 0.5  # коэффициент сопротивления воздуха
ro = 1.293  # плотность воздуха
S = constants.pi * ((6.6 / 2) ** 2)
g = 1.00034 * constants.g
k = (M - m0) / (2 * 60 + 48)  # скорость расхода топлива (через 3+- мин отсоединилась последняя ступень)


def A(t):
    return (Ft / (M - k * t))


def B(t):
    return ((Cf * ro * S) / (2 * (M - k * t)))


def dv_dt(t, v):
    return (A(t) - B(t) * v ** 2 - g)


v0 = 0

t = np.linspace(0, 56, 1080)

solve = integrate.solve_ivp(dv_dt, t_span=(0, max(t)), y0=[v0], t_eval=t)

x = solve.t
y = solve.y[0]

plt.figure(figsize=(7, 6))
plt.plot(x, y, '-r', label="v(t)")
plt.xlabel("Время (с)", fontsize=12)  # Подпись оси X
plt.ylabel("Скорость (м/с)", fontsize=12)  # Подпись оси Y
plt.title("Зависимость скорости от времени (мат. модель)", fontsize=14)  # Подзаголовок графика
plt.legend()
plt.grid(True)
plt.show()
