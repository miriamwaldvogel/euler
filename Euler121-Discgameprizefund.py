from math import factorial, ceil
def minfund(n):
    g = [[0 for i in range(j+1)] for j in range(1, n+1)]
    g[0][0] = 1
    g[0][1] = 1
    for i in range(n-1):
        for j, k in enumerate(g[i]):
            g[i+1][j] += k
            g[i+1][j+1] += (i+2)*k
    print(int(factorial(n+1)/sum(g[n-1][:ceil(n/2)])))

minfund(15)
