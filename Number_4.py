def schet(ineger):

    for i in range(1, ineger+1):
        if i == 1:
            print(" ", end="  ")
            for k in range(1,   ineger+1):
                if k < 10:
                    print(" " + str(k), end=" ")
                else:
                    print(str(k), end=" ")
            print("")
        if i < 10:
            print(" " + str(i), end=" ")
        if i >= 10:
            print(str(i), end=" ")
        for j in range(1, ineger+1):
            if j*i < 10:
                print(" " + str(j * i), end=" ")
            else:
                print(str(j * i), end=" ")
        print(" ")


schet(int(input("Выберите число до которого требуется вывести таблицу умножения ")))