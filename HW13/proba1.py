with open("src_14.txt", "r+", encoding="utf-8") as open_file:
    lst_text = open_file.read().split('\n')
    print(lst_text)
    lst_text.pop()
    print(lst_text)
    counter = summa = 0
    a = []
    name = []
    name1 = []
    name3 = []
    rating = []
    rating1 = []
    rating2 = []
    rating3 = []
    for i in lst_text:
        i = i.split()
        a.append(i)
    print(a)
    for i in a:
        counter += 1
        for j in i:
            if j.isdigit():
                num = int(j)
                summa += num
                rating.append(num)
            else:
                if j.isalpha() is True:
                    name.append(j)
    print(name)
    print(rating)
    line_length = len(rating)
    print("Количество оценок: ", line_length)
    summma_num = sum(rating)
    print("Сумма всех оценок учеников: ", summma_num)
    # Округляем знаячение средний оценки до сотых.
    average_score = round((summma_num / line_length), 2)
    print("Средний бал по классу", average_score)
    for i in range(0, len(name), 2):
        x = name[i] + ' ' + name[i + 1]
        name1.append(x)
    print(name1)  # Получили список учеников, состоящий из их имени и фамилии.
    start = 0
    for i in range(12):
        stop = start + len(rating[i::12])
        print(rating[start:stop])
        rating1.append(rating[start:stop])
        start = stop
    print(rating1)
    print(name1)
    for i in range(len(rating1)):
        summa_ocenok_uchenika = 0
        for j in range(12):
            summa_ocenok_uchenika = (summa_ocenok_uchenika + rating1[i][j])
        rating2.append(summa_ocenok_uchenika)
    print(rating2)
    for i in range(len(rating2)):
        sr_ocenka_uchenoka = round((rating2[i] / 12), 2)
        rating3.append(sr_ocenka_uchenoka)
    print(rating3)
    dictionary_class = dict(zip(name1, rating3))
    print(dictionary_class)
    print("Учащиеся класса, чей средний бал маньше 5:")
    for key, value in dictionary_class.items():
        if dictionary_class[key] < 5.0:
            print('{:<30} {}'.format(key, value))
    name2 = list(reversed(name))
    print(name2)
    for i in range(0, len(name2), 2):
        x = name2[i] + ' ' + name2[i + 1]
        name3.append(x)
    print(name3)
