class NegativeNumber(Exception):
    def __init__(self, text):
        self.txt = text


a = input("Введите положительное число: ")

try:
    a = int(a)
    if a < 0:
        raise NegativeNumber("Вы ввели отрицательное число!")
    elif a ==0:
        raise NegativeNumber("Вы ввели ноль!")
except ValueError:
    print("Вы ввели не число!")
except NegativeNumber as mr:
    print(mr)
else:
    print("Ура! Вы ввели положительное число: ",a)