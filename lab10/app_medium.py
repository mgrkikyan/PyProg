import tkinter as tk
from superpack import main_7_

# Создание окна
root = tk.Tk()

# Функция, вызываемая при нажатии на кнопку
def run_foo():
    try:
        value = int(entry.get())
        result = main_7_.func(value)
        output_label.config(text=f"i: {value}\n{result}")
    except ValueError:
        output_label.config(text="Введите целое число!")

# Создание текстовой метки
label = tk.Label(root, text="Введите целое число:")
label.pack()

# Создание поля ввода
entry = tk.Entry(root)
entry.pack()

# Создание кнопки
button = tk.Button(root, text="Запустить foo", command=run_foo)
button.pack()

# Создание метки для вывода результата
output_label = tk.Label(root, text="")
output_label.pack()

# Запуск главного цикла событий
root.mainloop()
