def tiles(n, l):
    w = [1]*l+[0]*(n-l+1)
    for i in range(l, n+1):
        w[i] += w[i-1]+w[i-l]
    return(w[n]-1)

def total(n):
    t = 0
    for i in range(2, 5):
        t += tiles(n, i)
    print(t)

total(50)
