with open("src_14.txt", "r+", encoding="utf-8") as open_file:
    lst_text = open_file.read().split('\n')
    print(lst_text)
    lst_text.pop()
    a = list()
    for i in lst_text:
        i = sorted(i.split(), key=str)
        a.append(i)
    print(a)
    for i in a:
        for j in i:
            j = [int(j) for j in i[:12]]
            a.insert(i, j)
    print(a)

