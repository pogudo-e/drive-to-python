import fractions


def check_d(a, b):
    # Сокращаем дроби
    q = a
    w = b
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return int(q / a), int(w / a)


def sum_d(arr):
    # Слаживаем дроби
    if arr[0][1] == arr[1][1]:
        q = arr[0][0] + arr[1][0]
        w = arr[0][1]
    else:
        q = (arr[0][0] * arr[1][1]) + (arr[0][1] * arr[1][0])
        w = arr[0][1] * arr[1][1]
    return q, w


num_one = input("Введите первую строку: ")
num_two = input("Введите вторую строку: ")

arr = [int(x) for x in num_one.split("/")], [int(x) for x in num_two.split("/")]

# Слаживаем дроби
q, w = sum_d(arr)

# Умножаем дроби
e = arr[0][0] * arr[1][0]
r = arr[0][1] * arr[1][1]

# Сокращаем дроби
q, w = check_d(q, w)
e, r = check_d(e, r)

one_f = fractions.Fraction(arr[0][0], arr[0][1])
two_f = fractions.Fraction(arr[1][0], arr[1][1])

# Работа с правильными и неправильными дробями при сложении
print('Сложение: ')
if q > w and q % w == 0:
    print(q // w)
else:
    print(f'\tРезультат: {q}/{w}')

print(f'\tПроверка: {one_f + two_f}')

print('Умножение: ')
print(f'\tРезультат: {e}/{r}')
print(f'\tПроверка: {one_f * two_f}')
