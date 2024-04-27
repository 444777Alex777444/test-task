def objii_delitel(array):
    k = []
    count = 0
    if min(array) != 1:
        for i in range(2, int(min(array)/2)+2):
            if i == int(min(array)/2)+1:
                i = min(array)
            for j in array:
                if j % i == 0:
                    count += 1
            if count == len(array):
                k.append(i)
            count = 0
        return k
    else:
        return [1]
kolvo = int(input("Введите количество элементов для которых надо найти общий делитель "))
array = []
for i in range(1, kolvo+1):
    array.append(int(input(f"Введите {i} элемент ")))
print(objii_delitel(array))
