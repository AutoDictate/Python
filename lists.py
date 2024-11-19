names = ["surya", "Yuvaraj", "Nagaraj", "bruno"]
# names.remove("bruno")
for bestFriend in names:
    print(bestFriend)

print("Last element of the list :", names[-1])

#Check the item exists
name = str(input("Give the name to check : "))
print(f"Is {name} is in the list ?", "YES" if {name} in names else "NO")

#sort list

def func(n):
    return n-50
li = [100, 50, 65, 82, 23]
# li.sort(key = func)
li.sort(reverse=True)
print(li)