def key_param(**kwargs) -> dict[str, str]:
    """
    Принимает на вход ключевые параметры и возвращает словарь,
    где ключ - значение переданного аргумента, а значение - имя аргумента
    :param kwargs: передаваемые аргументы
    :return: итоговый словарь
    """
    result = {}
    for key, value in kwargs.items():
        result[str(value)] = key
    return result


my_dict = key_param(Name="Alex", Years=26, Phone=12334546465, Balance=12.4, list_int=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(my_dict)
