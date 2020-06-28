def golden(n):
    a = 1
    b = 1
    for i in range(2*n-1):
        c = a
        a += b
        b = c
    print(a*c)

golden(15)
