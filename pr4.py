from random import randint
from time import time
computer_random = randint(1,500)
popitka = 0
start_time = time()

while True:
    user_point = input("Введите число для попытки (или 0 введите для выхода):")

    if user_point == "0":
        print("Выход из игры")
        break
    try:
        guess=int(user_point)
        popitka += 1
        if guess < computer_random:
            print("Загаданное число больше")
        elif guess > computer_random:
            print("Загаданное число меньше")
        else:
            end_time = time()
            print(f"Вы угадали число{computer_random} за {popitka} и {round(end_time-start_time)}")
            break
    except ValueError:
        print("Введите корректное число")

