def gen_f(a, b):  # Создаём функцию с двумя аргументами.
    """
       Функция генератор простых чисел в дипазоне заданным 2мя аргументами чисел.
    """
    if a < 2:  # Отсекаем единицу, т.к. она не является простым числом.
        a = 2
    for i in range(a, b + 1):  # Пробегаем все числа от a до b включительно.
        for j in range(2, i):  # Ищем делители среди списка чисел не превышающих делимое.
            if i % j == 0:  # Если делитель найден, число не простое.
                break  # Позволяет завершить выполнение внутреннего цикла и перейти к следующей итерации внешнего.
        else:
            yield i  # Если делителей нет выводим число пользователю.


# Цикл вывода показаний генератора в одну строку через пробел.
for n in gen_f(1, 100):
    print(n, end=' ')
