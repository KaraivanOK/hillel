text = input("Введите ваше предложение: ")
# Все знаки препинания, а также перенос строки меняем на пробел.
text = text.replace("\n", " ").replace(",", " ").replace(".", " ").replace("?", " ").replace("!", " ") \
    .replace(":", " ").replace(";", " ")
text = text.lower()  # Переводим весь текст в нижний регистр.
words = text.split()  # Разбиваем текст по пробелу.
words_dict = dict.fromkeys(words, 0)  # Создаём словарь с ключами из слов и начальным значением 0.
# Каждый раз при совпадении слова в строке и ключа в словаре будем добавлять в значение ключа +1.
for word in words:
    if word in words_dict:
        words_dict[word] = words_dict[word] + 1
    else:
        words_dict[word] = 1
print(words_dict)
