class Buffer:

    # Конструктор без аргументов.
    def __init__(self):
        # Список, в который будет добавляться последовательность целых чисел.
        self.current_part = []

    # Добавляет следующую часть последовательности.
    def add(self, *a):
        # Расширяем список, добавляя в него элементы.
        self.current_part.extend(a)
        while len(self.current_part) - 5 >= 0:
            # Выводим сумму первых 5-ти элементов списка.
            print(sum(self.current_part[0:5]))
            # Список принимает значения оставшихся элементов.
            self.current_part = self.current_part[5:]

    # Возвращает сохраненные в текущий момент элементы последовательности в
    # порядке, в котором они были добавлены.
    def get_current_part(self):
        return self.current_part


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()
