def numfractions(n):
    a = [i for i in range(n+1)]
    for i in range(2, n+1):
        if a[i] == i:
            for j in range(i, n+1, i):
                a[j] -= a[j]/i
    print(int(sum(a)-1))

numfractions(1000000)
