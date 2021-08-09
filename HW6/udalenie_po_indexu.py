import random  # Импортируем модуль random.

my_list1 = ([random.randint(0, 100) for i in range(0, 10)])  # Генерируем список из десяти случайных чисел.
print(my_list1)  # Выводим список пользователю.
k = int(input("Введите индекс числа в списке, которое хотите удалить: "))  # Просим пользователя ввести индекс.
i = 0  # Шаг необходимый только для сравнения вводимого индекса с заданным диапазоном.
while k < -(len(my_list1)) or k > (len(my_list1)-1):  # Выводим запрос на повторный ввод индекса, если он не в диапазоне.
    print("Введённый индекс не входит в диапазон.")
    k = int(input("Введите индекс числа в списке, которое хотите удалить: "))
    i = i + 1
if k in range(-(len(my_list1)), 0):  # Если пользователь ввёл отрицательный индекс, то преобразуем его в положительный.
    k = len(my_list1) + k
while k != len(my_list1) - 1:  # Меняем местами число в заданном индексе с числом в следующем индексе до тех пор
    # пока число не запишется в крайний элемент списка.
    my_list1[k], my_list1[k + 1] = my_list1[k + 1], my_list1[k]
    k = k + 1
my_list1.pop()  # Из перебранного списка удаляем крайний элемент.
print(my_list1)  # Выводим список с удалённым элементом.