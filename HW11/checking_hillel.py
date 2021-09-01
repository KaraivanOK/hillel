import hillel

print(help(hillel))
print('+' * 100, '\n')

print(help(hillel.built_in_collections1), '\n')
print(' ' * 50, 'CHECKING built_in_collection1\n')
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list1 = [0, 2, 4, 6, 100, 50, 80, 8, 9, 10]
k = 5
c = 100
print("1.Удалим из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.\n "
      "Ввод:\n", my_list, "\n", k, "\n Вывод:\n", hillel.delete_by_index(my_list, k))
print("2.Вставим в список на позицию с индексом k значение C, сдвинув все элементы, с индексом большим k, вправо.\n "
      "Ввод:\n", my_list, "\n", k, "\n", c, "\n Вывод:\n", hillel.insert_number(my_list, k, c))
print("3.Подсчитаем сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.\n "
      "Ввод:\n", my_list, "\n", my_list1, "\n Вывод:\n", hillel.amount_unique_numbers(my_list, my_list1))
print('+' * 100, '\n')

print(help(hillel.built_in_collections2), '\n')
print(' ' * 50, 'CHECKING built_in_collection2\n')
my_text = 'киви, банан, киви, апельсин, киви, банан'
my_text1 = 'абрикос,малина,абрикос'
my_text2 = 'малина, абрикос,абрикос'
my_list2 = [0, 1, 2, 5, 8, 10, 0, 2, 8]
my_list3 = [100, 50, 5, 8, 10, 40, 80]
print("1.Для каждого слова из заданного текста подсчитаем, сколько раз оно встречалось в этом тексте.\n "
      "Ввод:\n", my_text, "\n Вывод:\n", hillel.word_frequency(my_text))
print("2.Выведем слово, которое чаще всего встречается в трёх различных строках.\n "
      "Ввод:\n", my_text, "\n", my_text1, "\n", my_text2, "\n Вывод:\n",
      hillel.maximum_number_of_word_mentions(my_text, my_text1, my_text2))
print("3.Из заданного списка чисел определим сколько в нём встречается различных чисел.\n "
      "Ввод:\n", my_list2, "\n Вывод:\n", hillel.quantity_of_different_numbers(my_list2))
print("4.Задаются два списка чисел. Определим количество чисел, содержащихся как в первом списке, так и во втором.\n "
      "Ввод:\n", my_list2, "\n", my_list3, "\n Вывод:\n", hillel.confluence(my_list2, my_list3))
print('+' * 100, '\n')

print(help(hillel.func_module), '\n')
print(' ' * 50, 'CHECKING func_module\n')
my_list4 = [0, 1, 2, 3, 4, 5]
num = 9
a = 1
b = 100
print("1.Проверим есть ли в списке 2 числа, сума которых еквивалентна числу переданому 2м параметром.\n Ввод:\n",
      my_list4, "\n", num, "\n Вывод:\n", hillel.two_sum(my_list4, num))
print("2.Возьмём список с числами и возведём каждое число списка в квадрат.\n Ввод:\n",
      my_list4, "\n Вывод:\n", hillel.list_numbers_squared(my_list4))
print("3.Найдём простые числа в дипазоне заданным 2мя аргументами чисел.\n Ввод:\n",
      a, "\n", b, "\n Вывод:")
print(hillel.prime_number(a, b))
print('+' * 100, '\n')

print(help(hillel.sequence_sorting_module), '\n')
print(' ' * 50, 'CHECKING sequence_sorting_module\n')
print("1.Выведем заданное количество членов треугольной последовательности.\n Ввод:\n", 5, "\n Вывод:")
print(hillel.triangle_sequence(5))
print("2.Определим количество последовательностей из 0 и 1, где два нуля не стоят рядом! \nВвод:"
      " \nколичество нулей = 2 количество единиц = 2 \nВывод: \n", hillel.without_00(2, 2))
print("3.Развернём число! \nВвод: \n 179 \nВывод:\n", hillel.reverse_it(179))
print("4.Отсортируем матрицу!")
print(hillel.func_sort_matrix([
    [17, 38, 1, 25, 27, 1],
    [28, 21, 17, 6, 45, 44],
    [24, 36, 9, 2, 39, 1],
    [21, 18, 23, 46, 19, 22],
    [10, 14, 39, 5, 9, 31],
    [16, 26, 3, 32, 24, 34]], 6))
