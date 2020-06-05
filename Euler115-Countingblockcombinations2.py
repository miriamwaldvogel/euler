def blockcombos(n):
    w = [1]*(50)+[0]*(n-2)
    for i in range(50, n+1):
        w[i] = w[i-1]+sum(w[:i-50])+1
    return(w[n])

def driver(n):
    i = 51
    a = blockcombos(i)
    while a < n:
        i += 1
        a = blockcombos(i)
    print(i, a)

driver(1000000)
