import random  # Импортируем модуль random.

# Предлагаем пользователю ввести число.
M = int(input("Введите любое целое положительное число больше 5!: "))
massiv1 = []  # Создаём пустой список.


# Создаём функцию сортировки.
def func_sort(x):
    # Проверяем число на правильность ввода.
    while x < 5:
        print("Вы ввели число меньше 5! Повторите попытку.")
        x = int(input("Введите любое целое положительное число больше 5!: "))
    else:
        # Создаём матрицу, если число отвечает требованиям.
        massiv = [[random.randint(1, 50) for i in range(x)] for j in range(x)]
    print()
    print("До сортировки:")
    # Проходим по каждому столбцу матрицы и находим сумму его элементов.
    for i in range(x):
        s = 0
        for j in range(x):
            s += massiv[j][i]
        # Добавляем сумму элементов столбца в пустой список.
        massiv1.append(s)
    # Объединяем сгенерированную матрицу и одиночный список.
    massiv2 = massiv + [massiv1]
    # Матрица увеличивается на одну строку.
    for j in range(x + 1):
        for i in range(x):
            # Выводим полученную матрицу.
            print("%4d" % massiv2[j][i], end=' ')
        print()
    print()
    print("После сортировки:")
    k = x - 1
    while k > 0:
        ind = 0
        for i in range(k + 1):
            if massiv2[x][i] > massiv2[x][ind]:
                ind = i
        for j in range(x + 1):
            massiv2[j][ind], massiv2[j][k] = massiv2[j][k], massiv2[j][ind]
        k -= 1
    for i in range(x):
        for y in range(x - 1):
            for j in range(0, x - y - 1):
                if i % 2 == 1:
                    if massiv2[j][i] > massiv2[j + 1][i]:
                        massiv2[j][i], massiv2[j + 1][i] = massiv2[j + 1][i], massiv2[j][i]
                if i % 2 == 0:
                    if massiv2[j][i] < massiv2[j + 1][i]:
                        massiv2[j][i], massiv2[j + 1][i] = massiv2[j + 1][i], massiv2[j][i]
    for j in range(x + 1):
        for i in range(x):
            print("%4d" % massiv2[j][i], end=' ')
        print()


func_sort(M)
