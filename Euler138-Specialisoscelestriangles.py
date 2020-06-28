def triangles(n):
    a = 1
    b = 17
    t = 17
    for i in range(n-1):
        c = 18*b - a
        a = b
        b = c
        t += c
    print(t)

triangles(12)
