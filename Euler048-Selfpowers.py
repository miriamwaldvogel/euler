def selfpowers(n):
    t = 0
    for i in range(1, n+1):
        t += int(str(i**i)[-10:])
    print(str(t)[-10:])

selfpowers(1000)
