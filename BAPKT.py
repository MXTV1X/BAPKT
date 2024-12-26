import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import constants

# данные Кербина
m0 = 41904
M = m0 + 36482  # масса с топливом
Ft = 3268861.02  # тк сами рассчитать не смогли, взяли среднее из интернета
Cf = 0.5
ro = 1.293
S = constants.pi * ((6.6 / 2) ** 2)
g = 1.00034 * constants.g # ускорение свободного падения в KSP (на Кербине).
k = (M - m0) / (2 * 60 + 48)  # скорость расхода топлива (через 2 мин и 48 сек отсоединилась последняя ступень)



# функция для нахождения тяги двигателя
def A(t):
    return (Ft / (M - k * t))


# коэффициент аэродинамического сопротивления
def B(t):
    return ((Cf * ro * S) / (2 * (M - k * t)))


# дифференциальное уравнение для расчёта изменения скорости ракеты
def dv_dt(t, v):
    return (A(t) - g - B(t) * v ** 2)  # считаем, что изменение косинуса пренебрежимо мало


v0 = 0

t = np.linspace(0, 56, 1000)
# решение дифференциального уравнения (функция изменения скорости, интервал времени условия, начальная скорость, точки в которых вычисляются значения)
solve = integrate.solve_ivp(dv_dt, t_span=(0, max(t)), y0=[v0], t_eval=t)

x = solve.t
y = solve.y[0]

plt.figure(figsize=(7, 6))
plt.plot(x, y, '-r', label="v(t)")  # построение графика (линия)
plt.xlabel("Время (с)", fontsize=12)
plt.ylabel("Скорость (м/с)", fontsize=12)
plt.title("Зависимость скорости от времени (мат. модель)", fontsize=14)
plt.legend()
plt.grid(True)
plt.show()
