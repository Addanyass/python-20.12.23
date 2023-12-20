while True:
    a = int(input("Введите первое число диапазона: "))
    b = int(input("Введите второе число диапазона: "))
    c = int(input("Введите число: "))
    if c < a and c > b:
        break
    for i in range(a,b+1):
        if i == c:
            print('!' + str(c) + '!', end=" ")
            continue
        print(i, end=" ")
