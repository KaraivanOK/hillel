god = int(input("Введите год: "))  # Введение значения нужного года.
if god > 1900 and god < 1000000:   # Проверка на вхождение года в заданный диапазон.
    if god % 4 == 0 and god % 100 != 0 or god % 400 == 0:  # Проверка на соответствие параметрам високосного года по
        # григорианскому календарю.
        print("%s год - это високосный год." % god)  # Данный год високосный и входит в заданный диапазон.
    else:
        print("%s год - это невисокосный год." % god)  # Данный год невисокосный, но входит в заданный диапазон.
else:
    print("Введеный год не отвечает условиям!")  # Данный год не входит в заданный диапазон.
