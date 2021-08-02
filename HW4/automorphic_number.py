predel = int(input("Введите предел поиска автоморфных чисел: "))
mod = 10
for i in range(1, predel):
    if i == mod:
        mod *= 10
    if (i * i) % mod == i:
        print(i,'*',i,'=', (i*i))
