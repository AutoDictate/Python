for i in range(5):
    s=""
    for j in range(i+1):
        if j <= i:
            s+="*"
        else:
            s+=" "
    print(s)