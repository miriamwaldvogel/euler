def convergents(n):
    p = [1, 1, 4]
    a = 8
    b = 3
    i = 3
    t = 0
    while i < n:
        j = i%3
        c = b
        b = a
        a *= p[j]
        a += c
        if j == 2:
            p[2] += 2
        i += 1
    for i in str(a):
        t += int(i)
    print(t)

convergents(100)
