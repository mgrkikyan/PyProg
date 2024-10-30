import matplotlib.pyplot as plt
import numpy as np 

# Линейная зависимость
x = np.linspace(0, 10, 50)
y1 = x
y2 = [i**2 for i in x] # Квадратичная зависимость

# Построение графика
plt.title('Зависимости: y1 = x, y2 = x^2') # заголовок
plt.xlabel('x') # ось абсцисс
plt.ylabel('y1, y2') # ось ординат
plt.grid() # включение отображение сетки
plt.plot(x, y1, x, y2) # построение графика
plt.show()