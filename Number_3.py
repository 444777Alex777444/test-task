def light_chisla(array):
    k=[]
    for i in range(len(array)):
        count = 0
        for j in range(2, int((array[i]+1 )/2)+1):
            if array[i] % j == 0:
                count += 1
                if count > 0:
                    break
        if count == 0:
            k.append(array[i])
        count=0
    return k
array=[]
minimum =int(input("Введите минимальное число "))
maximun = int(input("Введите ммаксимальное число "))
for i in range(minimum, maximun + 1):
    array.append(i)
print(light_chisla(array))