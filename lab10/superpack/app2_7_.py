# Без использования рекурсии

def divide_list(numbers):
    even_list = []
    odd_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    return [odd_list, even_list]

numbers = [1, 2, 3, 4, 5]
result = divide_list(numbers)
print(result)
