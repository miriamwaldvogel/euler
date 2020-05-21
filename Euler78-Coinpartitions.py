def coinpartitions(n):
    k = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 250)], [])
    p = [1]
    sign = [1, 1, -1, -1]
    i = 0
    while p[i]>0:
        i += 1
        q = 0
        j = 0
        while k[j] <= i:
            q += p[i - k[j]] * sign[j%4]
            j += 1
        p.append(q % n)
    print(i)

coinpartitions(1000000)
