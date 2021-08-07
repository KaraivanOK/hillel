vvodimoe_chislo = int(input("Введите целое число от 3 до 9: "))  # Запрашиваем у пользователся число.
if vvodimoe_chislo >= 3 and vvodimoe_chislo <= 9:  # Проверяем введёное число на принадлежность заданному диапазону.
    for i in range(1, vvodimoe_chislo + 1): # Если число входит в диапазон, то задаём количество итераций с ограничением от 1 до вводимого числа включительно.
        for j in range(1, i + 1): # В каждой итерации создаём прямую последоваательность чисел в диапазоне от 1 до значения самой итерации включительно.
            print(j, end=" ") # Числа в данной последовательности в каждой итерации записаны через пробел.
        for j in range(i - 1, 0, -1): # В каждой итерации создаём обратную последоваательность чисел в диапазоне от значения самой итерации до нуля с шагом -1. При этом значения самой итерации и ноль не входят в диапазон.
            print(j, end=" ") # Числа в данной последовательности в каждой итерации записаны через пробел.
        print() # Выводим результат всех последовательностей в каждой итерации.
else: # Если введённое пользователем число не входит в диапазон от 3 до 9, выводим соответствующее сообщение.
    print("Введёное число не входит в заданный диапазон!")
