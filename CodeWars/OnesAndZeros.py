def binary_array_to_number(arr):
    res = 0
    for i in range(len(arr)):
        res +=  int(arr[len(arr)-i-1] * pow(2, i))
    return res


print(binary_array_to_number([0,0,0,1]))