def blockcombos(n):
    w = [1]*(3)+[0]*(n-2)
    for i in range(3, n+1):
        w[i] = w[i-1]+sum(w[:i-3])+1
    print(w[n])

blockcombos(50)
