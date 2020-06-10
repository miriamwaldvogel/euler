def fractionsrange(n):
    f = set()
    a = 1/3
    b = 1/2
    for i in range(2, n+1):
        for j in range(int(i/3), int(i/2)+1):
            c = j/i
            if a < c < b:
                f.add(c)
    print(len(f))

fractionsrange(12000)
