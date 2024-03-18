f_in = open("space.txt", encoding="UTF-8")
# извлечение заголовков
headers = f_in.readline()
arr = [elem.strip().split('*') for elem in f_in.readlines()]

query = input()
while query != "stop":
    for elem in arr:
        if elem[0] == query:
            spname, pla, coord, direc = elem
            break
    else:
        print("error.. er.. ror..")
        query = input()
        continue
    print(f"Корабль {spname} был отправлен с планеты: {pla} и его направление движения было: {direc}")
    query = input()
