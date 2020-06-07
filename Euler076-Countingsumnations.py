def sums(n):
    t =[0] * (n + 1)
    t[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            t[j] +=  t[j - i]

    print(t[n])
sums(100)
