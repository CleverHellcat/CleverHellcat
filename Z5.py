f_in = open("space.txt", encoding="UTF-8")
# извлечение заголовков
headers = f_in.readline()
slovar = dict()
counter = 0
for elem in f_in.readlines():
    elem = elem.strip()
    spname, pla, coord, direc = elem.split('*')
    slovar[pla] = slovar.get(pla, []) + [spname]
    if counter != 10:
        print('{' + pla + '}:{' + spname + '}')
        counter += 1

# print(slovar)