# Создаём класс счётчика.
class Counter:
    def __init__(self,
                 start=int(input("Введите начальное значение счётчика: ")),
                 end=int(input("Введите конечное значение счётчика: "))):
        self.start = start
        self.end = end

    def increase(self):
        # Применяем while, для цикличного вывода значений счётчика.
        while True:
            if self.start <= self.end:
                print(self.start)
                self.start += 1

            else:
                return 'Finish.'


my_count = Counter()
# В данном случае print выведет все значения счётчика, потому что в самом методе
# есть цикл. Для одиночного вывода значения можно для каждого значения
# прописывать print.
print(my_count.increase())
