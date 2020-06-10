def spiraldiags(n):
    t = 1
    a = 2
    s = 1
    for i in range(round((n-1)/2)):
        t += (10*a)+(4*s)
        b = a
        a += 2
        s += (4*b)
    print(t)

spiraldiags(1001)
