def delete_nth(order,max_e):
    pic = {}
    li = []

    for od in order:
        if od not in pic:
            pic[od] = 1

        if pic[od] <= max_e:
            li.append(od)
            pic[od]+=1


    return li

print(delete_nth([20, 37, 20, 21], 1))