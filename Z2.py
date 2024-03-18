def my_sort(arr:list) -> list:
    """Функция реализующая сортировку вставками.
    Функция возвращает отсортированный список

    :arg - неотсортированный список
    """
    i = 1
    while i < len(arr):
        j = 0
        while j < i:
            if arr[i] < arr[j]:
                arr = arr[:j] + [arr[i]] + arr[j:i] + arr[i+1:]
                break
            j += 1
        i += 1
    return arr


f_in = open("space.txt", encoding="UTF-8")
arr = [int(elem.split('*')[0].split('-')[-1]) for elem in f_in.readlines()[1:]]

arr = my_sort(arr)

for i in range(10):
    print(arr[i])
