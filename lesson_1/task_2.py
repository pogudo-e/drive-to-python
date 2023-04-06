from math import sqrt


def is_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    n = 0
    while 2 > n or n > 10000:
        n = int(input("Введите число: "))

    if is_prime(n):
        print("Простое число")
    else:
        print("Число НЕ является простым")
