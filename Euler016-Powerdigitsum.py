def powerdigitsum(n):
    s = 53
    a = str(2**s)[::-1]
    t = 0
    for i in range(s, n):
        b = ''
        for j in range(len(a)):
            e = 0
            if int(a[j-1]) > 4 and j > 0:
                e = 1
            d = str((int(a[j])*2)+e)
            b += d[-1]
        if len(d) > 1:
            b += d[0]
        a = b
        d = ''
    for i in range(len(a)):
        t += int(b[i])
    print(t)

powerdigitsum(1000)
