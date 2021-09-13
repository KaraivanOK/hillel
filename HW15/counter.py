# Создаём класс счётчика.
class Counter:
    def __init__(self,
                 start=int(input("Введите начальное значение счётчика: ")),
                 end=int(input("Введите конечное значение счётчика: "))):
        self.start = start
        self.end = end

    def increase(self):
        if self.start < self.end:
            self.start += 1
            return 'Увеличили значение счётчика на 1: ', self.start
        else:
            return 'Вы достигли максимального значения:', self.start

    def present_value(self):
        return 'Текущее значение счётчика: ', self.start


my_count = Counter()
print(my_count.present_value())
print(my_count.increase())
print(my_count.present_value())
print(my_count.increase())
print(my_count.present_value())
print(my_count.increase())
print(my_count.present_value())
print(my_count.increase())
print(my_count.present_value())
print(my_count.increase())
print(my_count.present_value())
print(my_count.increase())
print(my_count.present_value())
print(my_count.increase())
print(my_count.present_value())
print(my_count.increase())
print(my_count.present_value())
