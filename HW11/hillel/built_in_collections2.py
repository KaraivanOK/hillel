"""Модуль содержит функции для работы со встроенными коллекциями."""

__all__ = ['word_frequency', 'maximum_number_of_word_mentions',
           'quantity_of_different_numbers', 'confluence']


def word_frequency(text):
    """Для каждого слова из заданного текста подсчитывает, сколько раз оно
    встречалось в этом тексте."""
    text = text.replace("\n", " ").replace(",", " ").replace(".", " ") \
        .replace("?", " ").replace("!", " ") \
        .replace(":", " ").replace(";", " ")
    text = text.lower()  # Переводим весь текст в нижний регистр.
    words = text.split()  # Разбиваем текст по пробелу.
    # Создаём словарь с ключами из слов и начальным значением 0. Каждый раз при
    # совпадении слова в строке и ключа в словаре будем добавлять в значение
    # ключа +1.
    words_dict = dict.fromkeys(words, 0)
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def maximum_number_of_word_mentions(text_1, text_2, text_3):
    """Задаются три строки. Функция выводит слово, которое в этом тексте
    встречается чаще всего. Если таких
    слов несколько, выводит последнее."""
    text = text_1 + ' ' + text_2 + ' ' + text_3
    # Все знаки препинания, а также перенос строки меняем на пробел.
    text = text.replace("\n", " ").replace(",", " ").replace(".", " ") \
        .replace("?", " ").replace("!", " ") \
        .replace(":", " ").replace(";", " ")
    text = text.lower()  # Переводим весь текст в нижний регистр.
    words = text.split()  # Разбиваем текст по пробелу.
    # Создаём словарь с ключами из слов и начальным значением 0. Каждый раз при
    # совпадении слова в строке и ключа в словаре будем добавлять в значение
    # ключа +1.
    words_dict = dict.fromkeys(words, 0)
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    # Создаём список из ключей словаря. Индексом для которого служит список из
    # значений словаря. Индексом для списка значений словаря служит максимальное
    # значение. Если несколько ключей имеют максимальное значение(несколько слов
    # встречается максимальное количество раз), то выводим последнее слово. Для
    # чего разворачиваем оба списка, т.к. .index() возвращает положение первого
    # искомого элемента.
    return (list(reversed(words_dict.keys())))[list(reversed(
        words_dict.values())).index(max(dict.values(words_dict)))]


def quantity_of_different_numbers(nums):
    """Из заданного списка чисел определяет сколько в нём встречается различных
    чисел."""
    return len(set(nums))


def confluence(nums_1, nums_2):
    """Задаются два списка чисел. Определяем количество чисел, содержащихся как
     в первом списке, так и во втором."""
    return len((set(nums_1) & set(nums_2)))
