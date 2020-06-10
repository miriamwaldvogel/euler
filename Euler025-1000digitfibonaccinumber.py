def fibdigit(n):
    a = 1
    b = 1
    i = 2
    while len(str(a)) < n:
        c = a
        a += b
        b = c
        i += 1
    print(i)

fibdigit(1000)
