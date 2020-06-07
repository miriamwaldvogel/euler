def tetra(n):
    a = 0
    b = 0
    c = 0
    d = 1
    for i in range(n):
        e = a
        a = b
        b = c
        c = d
        d = e+a+b+c
    print(d)

tetra(50)
