def orderedfractions(m):
    t = 3/7
    n = 0
    b = 0
    for i in range(2, m+1):
        j = int(i*t)
        while j/i < t:
            a = j/i
            if b < a:
                b = a
                n = j
            j += 1
    print(n)

orderedfractions(1000000)
