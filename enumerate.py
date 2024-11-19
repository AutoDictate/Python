names = ["surya", "yuvaraj", "bala", "senthil", "guna"]
ages = [1,2,3,4,5,6,7]

for i, name in enumerate(names):
    print(f"{i+1}.{name.title()}")

combined = list(zip(names, ages))

for i, j in combined:
    print(f'{i.title()} is {j} years old')