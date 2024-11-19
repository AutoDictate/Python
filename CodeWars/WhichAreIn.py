def in_array(array1, array2):
    l: list = []

    for i in array1:
        for j in array2:
            if j.__contains__(i) and l.count(i) == 0 :
                l.append(i)
    l.sort()
    return l

print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))