num = int(input("Введите число: "))
b = num
res = ""

while b:
    ins = str(b % 16)

    match ins:
        case "10":
            res = "a" + res
        case "11":
            res = "b" + res
        case "12":
            res = "c" + res
        case "13":
            res = "d" + res
        case "14":
            res = "e" + res
        case "15":
            res = "f" + res
        case _:
            res = ins + res

    b //= 16

print(f"Получилось: 0x{res}\nПроверка hex(): {hex(num)}")
