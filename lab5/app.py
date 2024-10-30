import numpy as np 
import matplotlib.pyplot as plt

# Чтение данных из текстового файла
with open('lab5/file.txt', 'r') as file:
    data = file.readlines()

# Разделение координат на x и y
x = []
y = []
for line in data:
    line = line.strip().split('\t')
    x.append(float(line[0]))
    y.append(float(line[1]))

x0 = 0
y0 = 3.078427

# Построение графика функции
plt.plot(x, y, label='График функции')

plt.axhline(y0,  label='Касательная', color='r', linestyle='--')

plt.title('График функции с касательной, параллельной оси Ox')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()