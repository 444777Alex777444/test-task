def computer_count(comp):
    if  11 <= int(comp) <= 19:
        print(f"{comp} компьютеров")
    elif int(comp[-1])==2 or int(comp[-1])==3 or int(comp[-1])==4:
        print(f"{comp} компьютера")
    elif int(comp[-1]) == 1:
        print(f"{comp} компьютер")
    else:
        print(f"{comp} компьютеров")
comp = input("Введите число компьютеров ")
computer_count(comp)




