def expansions():
    a = 3
    b = 2
    t = 0
    for i in range(999):
        n = b
        b += a
        a += 2*n
        if len(str(a)) > len(str(b)):
            t += 1
    print(t)

expansions()
