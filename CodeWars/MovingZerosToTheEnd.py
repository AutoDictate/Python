def move_zeros(lst):
    l1: list = []
    l2: list = []

    for i in lst:
        if i != 0:
            l1.append(i)
        else:
            l2.append(i)

    l1.extend(l2)
    return l1

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))