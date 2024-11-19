def tower_builder(n_floors):
    li = []
    a = n_floors * 2 - 1
    for i in range(n_floors):
        s = ""
        for j in range(a):
            if j == n_floors - 1:
                s+= "*"
            elif (n_floors - i - 1) <= j <= (a - n_floors + i) and i != 0:
                s+= "*"
            else:
                s+= " "

        # print(s)
        li.append(s)

    return li

print(
    tower_builder(6)
)
