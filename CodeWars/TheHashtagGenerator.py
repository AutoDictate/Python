def generate_hashtag(s):
    if s is None or len(s) == 0:
        return False

    inp = str(s)
    val = inp.split(" ")

    res: str = ""

    for i in val:
        t = i.replace(" ", "")
        if len(t) == 0:
            continue
        res +=t.title()

    if len(res) >= 140:
        return False

    return "#"+res

print(generate_hashtag("    Hello     world   "))