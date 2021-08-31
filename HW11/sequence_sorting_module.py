"""модуль, в котором реализованны функции сортировки последовательностей."""

# Список атрибутов, которые могут быть подключены.
__all__ = ['triangle_sequence', 'without_00', 'reverse_it','func_sort_matrix']


def triangle_sequence(n):
    """Функция выводит заданное количество членов треугольной последовательности.
    num - текущее число для вывода. Вывод num начинается с единицы,т.к. сама последовательность начинается с единицы.
    k - количество уже выведенных чисел num.
    В цикле будем выводить num и увеличивать k на 1.
    Каждый раз когда количество выводы определённого числа будет равно этому числу, счётчик вывода обнуляется и мы
    переходим к следующему числу."""
    num = 1
    k = 0
    for i in range(n):
        print(num, end=' ')
        k = k + 1
        if k == num:
            k = 0
            num = num + 1
    return str('')


def without_00(a, b):
    """  Функция опеределяет, сколько существует последовательностей из a нулей и b единиц, в которых
  никакие два нуля не стоят рядом. При этом задаются два параметра функции:
  a - количество нулей;
  b - количество единиц."""
    if a > b + 1:
        return 0
    if a == 0 or b == 0:
        return 1
    return without_00(a, b - 1) + without_00(a - 1, b - 1)


def reverse_it(n, i=0):
    """ Функция разворачивает число. При этом задаются два параметра функции:
 n - число, которое вводит пользователь;
 i - второе число, в которое мы записываем первое число в обратном порядке.
 Для этого мы каждую итерацию рекурсии отделяем от n остаток применяя n%10  и добывляем его в i, тем самым увеличивая i
 с каждой итерацией. Параллельно с этим мы уменьшаем значение n применяя n//10.
 В конечном итоге это приводит к тому, что n = 0, а i приобретает вид развёрнутого числа n."""
    if n == 0:
        return i
    else:
        return reverse_it(n // 10, i * 10 + n % 10)

def func_sort_matrix(massiv, x):
    """Функция сортировки двухмерного списка МхМ (матрицы).
Функция находит сумму элементов столбцов и отсортировывает столбцы по возрастанию этих сумм, а также отсортировывает
каждый нечётный столбец по возрастанию значений снизу вверх, а каждый чётный столбец - сверху вниз. Выводит матрицу до
сортировки и после сортировки.
Значения massiv и x - задаётся пользователем, с клавиатуры:
   massiv - матрица с одинаковым количеством строк и столбцов;
   x - количество строк(столбцов) матрицы."""
    massiv1 = []
    # Проверяем число на правильность ввода.
    while x != len(massiv) and x != len(massiv[0]):
        return "Количество строк матрицы должно быть равно количеству столбцов!"
    else:
        print("До сортировки:")
        for i in range(x):
            s = 0
            for j in range(x):
                s += massiv[j][i]
            massiv1.append(s)
        # Объединяем сгенерированную матрицу и одиночный список.
        massiv2 = massiv + [massiv1]
        # Матрица увеличивается на одну строку.
        for j in range(x + 1):
            for i in range(x):
                # Выводим полученную матрицу.
                print("%4d" % massiv2[j][i], end=' ')
            print()
        print()
        print("После сортировки:")
        # Сортируем матрицу по возрастанию суммы элементов столбца
        k = x - 1
        while k > 0:
            ind = 0
            # Количество столбцов остаётся неизменным.
            for i in range(k + 1):
                if massiv2[x][i] > massiv2[x][ind]:
                    ind = i
            # Количество строк увеличивается на 1.
            # В последней строке хранятся суммы элементов столбцов.
            # Сортирем столбцы матрицы по последней строке.
            for j in range(x + 1):
                massiv2[j][ind], massiv2[j][k] = massiv2[j][k], massiv2[j][ind]
            k -= 1
        # Сортируем элементы в столбцах матрицы не затрагивая последнюю строку.
        for i in range(x):
            # Задаём количество проходов по внешнему циклу.
            for y in range(x - 1):
                # Задаём количество проходов по внутреннему циклу.
                for j in range(0, x - y - 1):
                    # Принимаем что нумерация столбцов, при визуальном просмотре матрицы начинается с 1.
                    # В самой матрице столбцы по прежнему начинают нумерацию с 0.
                    # Для того чтобы отсортировать каждый нечётный столбец по возрастанию значений снизу
                    # вверх, а каждый чётный столбец по возрастанию значений сверху вниз, записываем противоположные
                    # сравнения в каждое из условий.
                    if i % 2 == 1:
                        if massiv2[j][i] > massiv2[j + 1][i]:
                            massiv2[j][i], massiv2[j + 1][i] = massiv2[j + 1][i], massiv2[j][i]
                    if i % 2 == 0:
                        if massiv2[j][i] < massiv2[j + 1][i]:
                            massiv2[j][i], massiv2[j + 1][i] = massiv2[j + 1][i], massiv2[j][i]
        # Выводим полученную матрицу.
        for j in range(x + 1):
            for i in range(x):
                print("%4d" % massiv2[j][i], end=' ')
            print()
        return str('')
