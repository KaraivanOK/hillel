import random  # Импортируем модуль random.

# Генерируем два списка чисел.
a = [random.randint(0, 10) for i in range(0, 10)]
b = [random.randint(0, 10) for j in range(0, 10)]
print(a)
print(b)
# Определяем количество чисел, содержащихся как в первом списке, так и во втором.
print(len((set(a) & set(b))))
# Если не надо показывать списки пользователю, то код имеет следующий вид:
# print(len((set([random.randint(0, 10) for i in range(0, 10)]) & set([random.randint(0, 10) for i in range(0, 10)]))))
