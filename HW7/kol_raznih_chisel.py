import random  # Импортируем модуль random.

# Генерируем список чисел.
a = [random.randint(0, 10) for i in range(0, 10)]
print(a)
# Определяем количество различных чисел в списке.
print(len(set(a)))
# Если не надо показывать список пользователю, то код имеет следующий вид:
# print(len(set([random.randint(0, 10) for i in range(0, 10)])))
