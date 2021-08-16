def twoSum(nums, target):  # Создаём функцию с двумя параметрами.
    for x in range(0, len(nums)):  # Задаём диапазон индекса для первого числа в сумме.
        i = nums[x]  # Принимаем за первое число в сумме.
        j = target - i  # Принимаем за второе число через разность суммы и первого числа.
        for y in range(x + 1, len(nums)):  # Задаём диапазон для второго числа в сумме.
            if j == nums[y]:  # Если предполагаемое второе число находится в списке.
                return True  # Выводим True.
            else:
                continue  # В противном случае начинаем следующий проход цикла.
    #  Если после всех проходов цикла второго числа в нём так и не оказалось, то выводим False.
    return False


nums = [1, 2, 3, 4, 5]
print(nums)
target = 7
print(target)
print(twoSum(nums, target))

list1 = [5, 4, 3, 2, 1]
print(list1)
chislo1 = 10
print(chislo1)
print(twoSum(list1, chislo1))
