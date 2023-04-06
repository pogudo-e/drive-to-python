from random import randint

num = randint(0, 1000)


def randomizer(num):
    # print(num)  # Подсказка :)
    count = 10
    while count > 0:
        count -= 1
        n = int(input("Введите число: "))
        if n < num:
            print("БОЛЬШЕ")
        elif n > num:
            print("МЕНЬШЕ")
        else:
            print(f"Поздравляем! Вы угадали за {10 - count} попыток!")
            break

        print(f"У Вас осталось {count} попыток.")
    else:
        print(f"Очень жаль. Вы не смогли отгадать число {num}")


randomizer(num)
