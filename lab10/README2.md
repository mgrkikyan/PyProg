# Отчет 
## Задание 
Сложность:
Medium
Реализуйте GUI приложение на одном из актуальных фреймворков

## Функциональность
- Пользователь может ввести целое число в поле ввода.
- При нажатии на кнопку "Запустить foo" вызывается функция `run_foo()`.
- Функция `run_foo()` пытается преобразовать введенное значение в целое число.
- Если введенное значение не является целым числом, выводится сообщение "Введите целое число!".
- В противном случае вызывается функция `func()` из модуля `main_7_` с введенным значением.
- Результат выполнения функции отображается на метке вывода в формате "i: {value}\n{result}".



### Код

```python
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
```

## Результат 
```python
PS C:\Users\acer\Desktop\PyProg> & c:/Users/acer/Desktop/PyProg/myenv/Scripts/python.exe c:/Users/acer/Desktop/PyProg/lab10/app_medium.py
0
0
1.5
PS C:\Users\acer\Desktop\PyProg> 
```

# Источник
- Документация по библиотеке tkinter: [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)