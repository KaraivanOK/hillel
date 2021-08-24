def reverse_it(n, i):
    if n == 0:
        return i
    else:
        return reverse_it(n // 10, i * 10 + n % 10)


print("Ввод: \n 179 ")
print('-' * 10)
print("Вывод:")
print(reverse_it(179, 0))
