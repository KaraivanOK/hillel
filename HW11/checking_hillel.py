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