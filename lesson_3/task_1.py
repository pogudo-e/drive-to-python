def duplicate_elem(lst):
    return {a for a in set(lst) if lst.count(a) > 1}


elem = [10, 10, 23, 10, 123, 66, 78, 123, 12, 12, 12, 12, 36, 26, 96, 345, 567, 234, 657]

print(duplicate_elem(elem))
