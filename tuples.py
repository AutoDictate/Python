names = []

print("Enter 6 names of your friends")
for i in range(6):
    name = input(f"{i + 1}. Enter the name: ")
    names.append(name)

print(tuple(names))