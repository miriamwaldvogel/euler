def constant():
    d = 1
    c = 1
    n = 0
    t = 1
    a = 0
    while d < 10000000:
        n+=len(str(c))
        if n >= d:
            t *= int(str(c)[n-d-len(str(c))+1])
            d *= 10
            a += 1
        c += 1
    print(t)

constant()
