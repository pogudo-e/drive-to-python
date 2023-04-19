stuff = {"телефон": 1, "наушники": 1, "штаны": 3, "футболка": 2, "футболка_2": 2, "куртка": 5, "кепка": 1}
backpack_size = 7


def backpack(things: dict[str:int], size: int) -> list[list[str]]:
    pcs, weight = zip(*sorted(things.items(), key=lambda x: x[1], reverse=True))
    result, temp, temp_w = [], [], 0
    for index, w in enumerate(weight, 0):
        temp_w += w
        temp.append((pcs[index]))
        for index_n, wn in enumerate(weight[index:], index):
            if wn + temp_w <= size:
                temp_w += wn
                temp.append(pcs[index_n])
        result.append(temp)
        temp, temp_w = [], 0
    return result


print(backpack(stuff, backpack_size))
