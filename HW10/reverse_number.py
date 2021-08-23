def reverse_it(n):
    if n < 10:
        return n  # выход из рекурсии
    d = n % 10
    r = reverse_it(n // 10)
    dd = 1  # Количество вхождений в рекурсию.
    r2 = r
    if r2 > 10:
        r2 //= 10
        dd += 1
    return d * (10 ** dd) + r

print("Ввод: \n 179 ")
print('-' * 10)
print("Вывод:")
print(reverse_it(179))
