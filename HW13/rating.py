# Открываем тестовый файл, который нам дан.
with open("src_14.txt", "r+", encoding="utf-8") as open_file:
    # Разделяем текст по переносу строки. Тем самым получаем строки, состоящие
    # из Имени Фамилии и оценок ученика.
    lst_text = open_file.read().split('\n')
    # Удаляем пустую строку из списка.
    lst_text.pop()
    # Создаём вспомогательные списки.
    a = []  # Помогает при разбиении строк.
    # Списки для имён.
    name = []
    name1 = []
    name2 = []
    name3 = []
    # Списки для оценок.
    rating = []
    rating1 = []
    rating2 = []
    rating3 = []
    # Разделяем строки списка по пробелу.
    for i in lst_text:
        i = i.split()
        a.append(i)
    for i in a:
        for j in i:
            # Из списка выделяем оценки и добавляем им в список с оценками.
            if j.isdigit():
                num = int(j)
                rating.append(num)
            else:
                # Из списка выделяем имена и добавляем их в список имён.
                if j.isalpha() is True:
                    name.append(j)
    # Определяем количество оценок в классе.
    line_length = len(rating)
    # Находим сумму всех оценок учеников класса.
    summma_num = sum(rating)
    # Округляем знаячение средний оценки до сотых.
    average_score = round((summma_num / line_length), 2)
    print("Средний балл по классу: ", average_score)
    # Объединяем Имя и Фамилию учеников и добавляем их в новый список.
    for i in range(0, len(name), 2):
        x = name[i] + ' ' + name[i + 1]
        name1.append(x)
    # Создаём матрицу из оценок ученика.
    # Каждый вложенный список состоит из оценок одного ученика.
    start = 0  # Точка отсчёта при создании вложенных списков.
    for i in range(12):
        stop = start + len(rating[i::12])
        rating1.append(rating[start:stop])
        start = stop
    # Находим сумму оценок каждого ученика.
    for i in range(len(rating1)):
        summa_ocenok_uchenika = 0
        for j in range(12):
            summa_ocenok_uchenika = (summa_ocenok_uchenika + rating1[i][j])
        rating2.append(summa_ocenok_uchenika)
    # Находим среднюю оценку ученика.
    for i in range(len(rating2)):
        sr_ocenka_uchenoka = round((rating2[i] / 12), 2)
        rating3.append(sr_ocenka_uchenoka)
    # Создаём словарь, в котором ключи - имена учеников, а значения - их оценки.
    dictionary_class = dict(zip(name1, rating3))
    print("Учащиеся класса, чей средний балл маньше 5:")
    # Находим учащихся, чей средний бал меньше 5.
    for key, value in dictionary_class.items():
        if dictionary_class[key] < 5.0:
            print('{:<30} {}'.format(key, value))
    # Делаем срез имён учеников по первой букве и добавляем точку.
    for i in range(0, len(name), 2):
        x = name[i][0] + '.'
        # Записываем в новый список.
        name2.append(x)
    # Достаём из списка фамилии учеников и также записываем в новый список.
    for i in range(1, len(name), 2):
        name3.append(name[i])
    # Объединяем список с фамилиями учеников и сокращённые имена учеников.
    name4 = [' '.join(item) for item in zip(name3, name2)]
    # Создаём словарь из Фамилия_Сокращённое имя. и средней оценки ученика.
    dictionary_class1 = dict(zip(name4, rating3))
# Создаём текстовый документ - Табель класса.
with open('tabel_classa.txt', 'w', encoding='utf-8') as tabel_classa:
    # Записываем в него словрь из Фамилия_Сокр.имя. и средней оценки ученика.
    for key, val in dictionary_class1.items():
        tabel_classa.write('{:<30} {}\n'.format(key, val))
