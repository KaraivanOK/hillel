import random

M = int(input("Введите любое целое положительное число больше 5!: "))
massiv1 = []
while M < 5:
    print("Вы ввели число меньше 5! Повторите попытку.")
    M = int(input("Введите любое целое положительное число больше 5!: "))
else:
    massiv = [[random.randint(1, 50) for i in range(M)] for j in range(M)]
print()
print("До сортировки:")
for i in range(M):
    s = 0
    for j in range(M):
        s += massiv[j][i]
    massiv1.append(s)
massiv2 = massiv + [massiv1]
for j in range(M + 1):
    for i in range(M):
        print("%4d" % massiv2[j][i], end=' ')
    print()
print()
print("После сортировки:")
k = M - 1
while k > 0:
    ind = 0
    for i in range(k + 1):
        if massiv2[M][i] > massiv2[M][ind]:
            ind = i
    for j in range(M + 1):
        massiv2[j][ind], massiv2[j][k] = massiv2[j][k], massiv2[j][ind]
    k -= 1
for j in range(M + 1):
    for i in range(M):
        print("%4d" % massiv2[j][i], end=' ')
    print()
print()
print()
