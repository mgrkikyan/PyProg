from functools import wraps

def range_checker(min=None, max=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if min is not None and max is not None:
                if not (min <= args[0] <= max):
                    print("Аргумент не находится в допустимом диапазоне")
                    return
            return func(*args, **kwargs)
        return wrapper
    # Проверяем, вызван ли декоратор с параметрами или без
    if callable(min):
        # Декоратор вызван без параметров, min является функцией
        func = min
        min, max = None, None
        return decorator(func)
    else:
        return decorator

# Пример использования декоратора с параметрами
@range_checker(min=0, max=10)
def test(value):
    print(f"Аргумент {value} находится в допустимом диапазоне")

# Пример использования декоратора без параметров
@range_checker
def test_no_range(value):
    print(f"Аргумент {value} обработан без проверки диапазона")

test(5)  # Аргумент 5 находится в допустимом диапазоне
test(15)  # Аргумент не находится в допустимом диапазоне
test_no_range(100)  # Аргумент 100 обработан без проверки диапазона