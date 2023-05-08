def gen_fib(number):
    number_fibo1 = 0
    number_fibo2 = 1
    for key in range(0, number):
        number_fibo_sum = number_fibo1 + number_fibo2
        number_fibo2 = number_fibo1
        number_fibo1 = number_fibo_sum
        key += 1
        yield number_fibo2


n = int(input('Введите сколько чисел Фибоначчи вывести на экран: '))
for i, num in enumerate(gen_fib(n), start=1):
    if i == n:
        print(num, end='')
    else:
        print(num, end=', ')
