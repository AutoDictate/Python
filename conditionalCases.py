
def validate_age(_age):
    if _age > 18:
        print("Eligible to vote")
    elif not (_age != 18 and _age != 17):
        print("Try to get Voter ID")
    else:
        print("Not Eligible to Vote")

age = int(input("Enter the age : "))
validate_age(age)

"""
    This is a multi-line comment
"""