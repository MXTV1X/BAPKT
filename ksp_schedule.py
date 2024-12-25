import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

y = [0, 84.7, 158.8, 245.3, 332.5, 406.3, 511.8, 636.4]  # Исходные точки X (м/с)
x = [0, 8, 16, 24, 32, 40, 48, 56]  # Исходные точки Y (с)

# Подготовка данных для сглаживания
x_smooth = np.linspace(min(x), max(x), 200)  # Новый массив X с большим числом точек
spl = make_interp_spline(x, y, k=3)  # Интерполяция (k=3 для кубического сплайна)
y_smooth = spl(x_smooth)  # Расчёт сглаженных Y

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x_smooth, y_smooth, color='red', label='Сглаженный график')  # Плавная линия
plt.title("Зависимость скорости от времени (KSP)", fontsize=14)
plt.xlabel("Время (с)", fontsize=12)
plt.ylabel("Скорость (м/с)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()