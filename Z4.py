def get_psw(spname: str, pla):
    """Функция """
    name, code = spname.split('-')
    return (pla[-3:] + name[1:-1] + pla[:3][::-1]).upper()


with open("space_uniq_password.csv", 'w') as f_out:
    # считывание входного файла в режиме чтения
    f_in = open("space.txt", encoding="UTF-8")

    # извлечение заголовков и запись их в f_out
    headers = f_in.readline().rstrip()
    print(headers + "*password", file=f_out)

    for elem in f_in.readlines():
        elem = elem.strip()
        spname, pla, coord, direc = elem.split('*')
        print(f"{elem}*{get_psw(spname, pla)}", file=f_out)
