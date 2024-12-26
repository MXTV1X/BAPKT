import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

y = [0, 84.7, 158.8, 245.3, 332.5, 406.3, 511.8, 636.4]
x = [0, 8, 16, 24, 32, 40, 48, 56]
# Подготовка данных для сглаживания
x_smooth = np.linspace(min(x), max(x), 1000
spl = make_interp_spline(x, y, k=3)  # Интерполяция (кубический сплайн обеспечивает гладкое соединение между точками данных)
y_smooth = spl(x_smooth)  # расчёт сглаженных Y для нового массива X

# Построение графика
plt.figure(figsize=(7, 6))
plt.plot(x_smooth, y_smooth, color='red', label='v(t)')
plt.xlabel("Время (с)", fontsize=12)
plt.ylabel("Скорость (м/с)", fontsize=12)
plt.title("Зависимость скорости от времени (KSP)", fontsize=14)
plt.legend()
plt.grid(True)
plt.show()
