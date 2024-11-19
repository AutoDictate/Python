def high(x) -> str:
    max = 0
    word = ""
    s = x.split(' ')
    for i in s:
        w = sum(ord(c) - ord('a') + 1 for c in i)
        if w > max:
            max = w
            word = i

    return word

print(high('man i need a taxi up to ubud'))

