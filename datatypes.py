from types import NoneType

a = 1       # int
b = 1.123   # float
c = "demo"  # str
d = 1j      # complex
e = [1, 2, 3]   # list
f = (1, 2, 3)   # tuple
g = range(6)    # range
h = {1, 2, 3}   # set
i = {"name": "surya", "gender": "male", "age": 23}  # dict
j = b"demo"     # bytes
k = NoneType    # type

l = [a,b,c,d,e,f,g,h,i,j,k]
for types in l:
    print(types, type(types))