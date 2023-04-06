
def triangle_check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            return "Треугольник равносторонний"
        elif a == b and b != c or c == a and b != a:
            return "Треугольник равнобедренный"
        else:
            return "Треугольник разносторонний"
    else:
        return "Треугольник не существует"


if __name__ == "__main__":
    print('Введите длины сторон треугольника:')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    print(triangle_check(a, b, c))
