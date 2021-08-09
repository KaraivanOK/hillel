import random  # Импортируем модуль random.

# Создаём два сгенерированных списка.
list_1 = [random.randint(0, 10) for i in range(0, 10)]
list_2 = [random.randint(0, 10) for i in range(0, 10)]
# Создаём список из элементов, которые не повторяются ни в одном из сгенерированных списков и находим длину этого
# списка.
print(len([x for x in (list_1 + list_2) if (list_1 + list_2).count(x) == 1]))