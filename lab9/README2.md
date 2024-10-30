## Отчет по тестированию генератора погоды

## Задание 
Сложность:
Medium
Напишите для генератора тесты с помощью pytest

### Тестирование функции weather_generator

### Код
```python
import pytest
from app import weather_generator

def test_weather_generator(mocker):
    cities = ["London", "Paris"]
    api_key = "test_api_key"
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"temp": 20, "weather": "Cloudy"}

    with mocker.patch('requests.get', return_value=mock_response):
        generator = weather_generator(cities, api_key)
        data = next(generator)
        assert data == {"temp": 25, "weather": "Cloudy"}
```

1. **Тест на получение данных о погоде для городов London и Paris:**
    - Входные данные: cities = ["London", "Paris"], api_key = "test_api_key"
    - Ожидаемый результат: {"temp": 25, "weather": "Cloudy"}
    - Фактический результат: {"temp": 20, "weather": "Cloudy"}
    - Статус: **Не пройден**

### Результат

```python
$ pytest test_weather_generator.py                                                                      
========================================= test session starts =========================================
platform win32 -- Python 3.10.9, pytest-8.2.0, pluggy-1.5.0
rootdir: C:\Users\acer\Desktop\PyProg\lab9
plugins: mock-3.14.0
collected 0 items / 1 error

=============================================== ERRORS ================================================
_____________________________ ERROR collecting test_weather_generator.py ______________________________
test_weather_generator.py:2: in <module>
    from app import weather_generator
app.py:14: in <module>
    city = input("Введите название города ('exit' для выхода из строки ввода): ")
..\myenv\lib\site-packages\_pytest\capture.py:207: in read
    raise OSError(
E   OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
------------------------------------------- Captured stdout ------------------------------------------- 
Введите название города ('exit' для выхода из строки ввода):
======================================= short test summary info ======================================= 
ERROR test_weather_generator.py - OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
========================================== 1 error in 0.73s =========================================== 
```

Pytest работает. Он выдает ошибку

### Список источников 
1. [Задумка с погодой](https://habr.com/ru/articles/315264/)

2. [Генераторы](https://habr.com/ru/articles/560300/)


