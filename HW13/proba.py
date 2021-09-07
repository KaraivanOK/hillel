with open("src_14.txt", "r+", encoding="utf-8") as open_file:
    lst_text = open_file.read().split('\n')
    print(lst_text)
    counter = summa = 0
    for line in lst_text:
        counter += 1
        length_line = len(line)
        for i in range(length_line):
            if line[i].isdigit():
                num = int(line[i])
                summa += num
                if num < 5:
                    print("Ученик(ца) у которого средний бал по классу меньше "
                          "3-х:", line)
            break
