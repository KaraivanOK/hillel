def count_first(n):
    num = 1  # Текущее число для вывода.
    k = 0  # Количество уже выведенных чисел cur.
    #  В цикле будем выводить cur и увеличивать k на 1
    # Каждый раз когда количество выводы определённого числа будет равно этому числу,
    # счётчик вывода обнуляется и мы переходим к следующему числу.
    for i in range(n):
        print(num, end=' ')
        k = k + 1
        if k == num:
            k = 0
            num = num + 1
    return count_first


print("Ввод: \n 2 ")
print("Вывод:")
count_first(2)
print()
print('-' * 10)
print("Ввод: \n 5 ")
print("Вывод:")
count_first(5)
