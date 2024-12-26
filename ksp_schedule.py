import numpy as np # для работы с массивами и числовыми вычислениями
import matplotlib.pyplot as plt # для построения графика
from scipy.interpolate import make_interp_spline # для сглаживания

y = [0, 84.7, 158.8, 245.3, 332.5, 406.3, 511.8, 636.4]  # значения скорости (м/с)
x = [0, 8, 16, 24, 32, 40, 48, 56]  # значения времени (с)

# Подготовка данных для сглаживания
x_smooth = np.linspace(min(x), max(x), 1000)  # массив точек для сглаживания
spl = make_interp_spline(x, y, k=3)  # Интерполяция (кубический сплайн обеспечивает гладкое соединение между точками данных)
y_smooth = spl(x_smooth)  # расчёт сглаженных Y для нового массива X

# Построение графика
plt.figure(figsize=(7, 6)) # размеры графика в дюймах
plt.plot(x_smooth, y_smooth, color='red', label='Сглаженный график')  # Плавная линия
plt.xlabel("Время (с)", fontsize=12)  # Подпись оси X
plt.ylabel("Скорость (м/с)", fontsize=12)  # Подпись оси Y
plt.title("Зависимость скорости от времени (KSP)", fontsize=14)  # Подзаголовок графика
plt.legend() # смысл линии (v(t))
plt.grid(True) # сетка на графике
plt.show() # отображение графика в окне
