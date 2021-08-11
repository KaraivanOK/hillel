import random  # Импортируем модуль random.

# Генерируем два списка.
a = [random.randint(0, 10) for i in range(0, 10)]
b = [random.randint(0, 10) for i in range(0, 10)]
print(a)
print(b)

# Определяем количество различных чисел в каждом отдельно взятом списке.
print(len(set(a)))
print(len(set(b)))

# Определяем количество различных чисел в обоих списках одновременно.
print(len(set(a + b)))

# Если отсутствует необходимость показать сгенерированный список пользователю, то можно вставить сам генератор в строку
# вывода.
print(len(set([random.randint(0, 10) for i in range(0, 10)])))
print(len(set([random.randint(0, 10) for i in range(0, 10)] + [random.randint(0, 10) for i in range(0, 10)])))
