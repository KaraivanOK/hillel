"""Модуль содержит функции для работы со встроенными коллекциями."""

__all__ = ['delete_by_index', 'insert_number', 'amount_unique_numbers']


def delete_by_index(my_list, k):
    """Удаляет из списка элемент с индексом k, сдвинув влево все элементы,
    стоящие правее элемента с индексом k.
     my_list - список, из которого необходимо удалить элемент. k - индекс
     элемента, который необходимо удалить.
"""

    while k < -(len(my_list)) or k > (len(my_list) - 1):
        return "Введённый индекс не входит в диапазон."
    else:
        if k in range(-(len(my_list)), 0):
            k = len(my_list) + k
        while k != len(my_list) - 1:
            my_list[k], my_list[k + 1] = my_list[k + 1], my_list[k]
            k = k + 1
        my_list.pop()
        return my_list


def insert_number(my_list, k, c):
    """Вставляет в список на позицию с индексом k значение C, сдвинув все
    элементы, с индексом большим k, вправо."""
    my_list.append(c)  # Добавляем новый элемент списка со значением 'С'.
    j = len(my_list) - 1  # Индекс числа 'с' в списке.
    while k < -(len(my_list) - 1) or k > (len(my_list) - 2):
        return "Введённый индекс не входит в диапазон."
    else:
        if k in range(-(len(my_list)), 0):
            k = len(my_list) + (k - 1)
        while j != k:
            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            j = j - 1
        return my_list


def amount_unique_numbers(my_list1, my_list2):
    """Подсчитывает сколько уникальных чисел содержится одновременно как в
    первом списке, так и во втором."""
    return len([x for x in (my_list1 + my_list2) if (my_list1 +
                                                     my_list2).count(x) == 1])
