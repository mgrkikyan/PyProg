import itertools

def A():
    """
    Функция считает количество допустимых слов.

    >>> A()
    276480

    :return: Количество допустимых слов.
    """
    S = ['В', 'И', 'Ш', 'Н', 'Я']
    L = ['И', 'Я']
    count = 0

    for i in itertools.product(S, repeat=6):
        if i.count('В') <= 1 and i[0] != 'Ш' and i[4] not in L:
            count += 1

    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
