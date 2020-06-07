def almosttriangles(n):
    a = 1
    b = 1
    c = 0
    d = 0
    e = 1
    while d <= n:
        f = b
        b = 4*b - a + 2*e
        a = f
        e = -e
        c += d
        d = 3*b - e
    print(c)

almosttriangles(1000000000)
