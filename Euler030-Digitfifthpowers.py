def npowers(n):
    t = 0
    for i in range(2, 999999):
        s = str(i)
        f = 0
        for j in s:
            f += int(j)**n
        if f == i:
            t += i
    print(t)

npowers(5)
