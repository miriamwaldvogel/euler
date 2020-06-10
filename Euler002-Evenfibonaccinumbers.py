def evenfibs(n):
    a = 1
    b = 1
    f = 0
    i = 0
    while i < n:
        f = a+b
        a = f+b
        b = a+f
        i += f
    print(i)

evenfibs(4000000)
