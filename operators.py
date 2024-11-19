c1 = 10
c2 = 30

c3 = int

l1 = [1,2,3]
l2 = [1,3,3,1]
l2.remove(2)
l3 = l2
l4 = list


if len(l3) > 1:
    l4 = l3
    print(l4)
    print("c1 is none")

print(l1 == l2) #False
print(l3 is l2) #True
print(c1 == c2) #False