# открытие выходного файла на запись
with open("space_new.txt", 'w') as f_out:
    # считывание входного файла в режиме чтения
    f_in = open("space.txt", encoding="UTF-8")

    # извлечение заголовков и запись их в f_out
    f_out.write(f_in.readline())

    for elem in f_in.readlines():
        # подготовка переменных для дальнейшей работы с ними
        elem = elem.strip()
        spname, pla, coord, direc = elem.split('*')
        coord = [int(val) for val in coord.split()]
        d_x, d_y = map(int, direc.split())
        code, (n, m, *_) = spname.split('-')
        n, m = int(n), int(m)

        # запись исправленных данных в выходной файл
        if all(coord):
            print(elem, file=f_out)
        else:
            #  исправляем координаты, используя данную формулу
            t = len([0 for letter in pla if letter.isalpha()])
            if n > 5:
                x = n + d_x
            else:
                x = -(n + d_x) * 4 + t
            if m > 3:
                y = m + t + d_y
            else:
                y = -(n + d_y) * m

            # запись измененных данных в выходной файл
            f_out.write(f"{spname}*{pla}*{x} {y}*{d_x, d_y}\n")

        # проверка условия для вывода строк в консоль
        if code.endswith('V'):
            print(f"{spname} - ({x}, {y})")
