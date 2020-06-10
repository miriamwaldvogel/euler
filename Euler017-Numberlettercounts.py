def numberlettercounts(n):
    d = [0]*(n+1)
    a = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8, 6, 6, 5, 5, 5, 7, 6, 6]
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]
    for i, j in zip(a, b):
        d[j] = i
    for i in range(21, 100):
        t = int(i/10)*10
        d[i] = d[t]+d[i-t]
    for i in range(100, n):
        h = int(i/100)
        t = i-h*100
        if t == 0:
            d[i] = d[h]+7
        else:
            d[i] = d[h]+10+d[t]
    d[1000] = 11
    print(sum(d))

numberlettercounts(1000)
