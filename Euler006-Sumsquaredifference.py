def sumsquare(n):
    print(int((((n+1)*n)/2)**2)-sum([i**2 for i in range(1, n+1)]))

sumsquare(100)
