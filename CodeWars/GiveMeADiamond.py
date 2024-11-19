def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None

    l = []
    m = n // 2

    for i in range(m + 1):
        s = " " * (m - i) + "*" * (2 * i + 1)
        l.append(s)

    for i in range(m - 1, -1, -1):
        s = " " * (m - i) + "*" * (2 * i + 1)
        l.append(s)

    word = "\n".join(l) + "\n"
    return word

print(diamond(5))
