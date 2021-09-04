def concantenation(x, y):
    """ Функция использует обрабатку исключений, запрашивая ввод двух значений.
    Если хотя бы одно из них не является числом, то выполняется конкатенация, то
    есть соединение, строк. В остальных случаях введенные числа суммируются."""

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return str(x) + str(y)
    except TypeError:
        return str(x) + str(y)
    else:
        return x + y
