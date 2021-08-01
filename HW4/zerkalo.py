slova = input("Введите два слова: ")
slova1 = slova.split()
kol_slov = len(slova1)
cifra1 = slova1[0].isdigit()
cifra2 = slova1[-1].isdigit()
if cifra1 == True or cifra2 == True:
    print("Вы ввели цифры. Введите только два слова!")
elif kol_slov > 2:
    print("Это количество слов превышает необходимое. Введите только два слова!")
elif kol_slov == 1:
    print("Это количество слов недостаточно. Введите только два слова!")
else:
    slova = slova[::-1].title()
    print(slova)
