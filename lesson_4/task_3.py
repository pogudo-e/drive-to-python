cash = 0
operation_count = 0


def check_operation_count() -> None:
    """
    Начисление процентов при определенном количестве операций.
    :return: None
    """
    global cash
    global operation_count
    if operation_count == 3:
        operation_count = 0
        cash += cash * 1.03
        print("Спасибо что выбрали нас. Мы пополнили ваш счет на 3%.")
        show_balance()
    else:
        operation_count += 1


def shut_up_and_take_my_money():
    """
    Налог на богатство, забирает 10% при балансе свыше 5000000
    :return: None (только забирает)
    """
    global cash
    if cash > 5000000:
        print("Ты слишком богат. Заберем ка 10%. Ты еще заработаешь.")
        cash = cash - (cash * 0.1)
        show_balance()


def show_balance() -> None:
    """
    Отображение баланса
    :return: None
    """
    global cash
    print(f"Баланс вашего счета составляет: {cash} у.е.")


def up_cash() -> None:
    """
    Пополнение счета. Пополнение происходит при определенных условиях.
    :return: None
    """
    global cash

    show_balance()
    shut_up_and_take_my_money()

    while True:
        value = input("Введите сумму пополнения счета или exit для выхода: ")
        if value == "exit":
            break
        else:
            value = int(value)
        if value % 50 != 0:
            print("Некорректный ввод. Сумма пополнения должна быть кратна 50 у.е.")
            continue
        else:
            cash = cash + value
            break
    check_operation_count()


def get_cash() -> None:
    """
    Снятие наличных. Снятие происходит при определенных условиях.
    :return: None.
    """
    global cash

    show_balance()
    shut_up_and_take_my_money()

    while True:
        value = input("Введите сумму для снятия или exit для выхода: ")
        if value == "exit":
            break
        else:
            value = int(value)
        percent = value * 0.015
        if percent < 30:
            percent = 30
        elif percent > 600:
            percent = 600
        if value % 50 != 0:
            print("Некорректный ввод. Сумма снятия должна быть кратна 50 у.е.")
            continue
        else:
            if cash < value + percent:
                print(f"Недостаточно средств. Введите сумму, меньше {cash + percent} (с учетом налогов).\n")
            else:
                cash = cash - value - percent
                break
    check_operation_count()


def close_program() -> None:
    """
    Останавливает работу программы.
    Предварительно показывает баланс и забирает деньги при определенных условиях.
    :return: None
    """
    show_balance()
    shut_up_and_take_my_money()

    import sys
    print("Всего доброго!")
    sys.exit()


def run():
    """
    Основная часть программы.
    """
    while True:
        choice = input("Выберите действие:\n1. Пополнить счет\n2. Снять наличные\n3. Проверить баланс\n"
                       "0. Завершить программу\n")
        if choice == "1":
            up_cash()
        elif choice == "2":
            get_cash()
        elif choice == "3":
            show_balance()
        elif choice == "0":
            close_program()
        else:
            print("Некорректный ввод. Введите 1, 2, 3 или 0.")


run()
