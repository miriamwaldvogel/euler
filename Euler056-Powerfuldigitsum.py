def maxdigitsum():
    s = 0
    for i in range(100):
        for j in range(100):
            n = i**j
            a = 0
            for k in str(n):
                a += int(k)
            if s < a:
                s = a
    print(s)

maxdigitsum()
