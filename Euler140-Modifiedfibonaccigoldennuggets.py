def golden(n):
    g = [7, 14, 50, 97]
    s = 5**0.5
    for i in range(4, n):
        g.append(7*g[i-2]-g[i-4])
    print(sum(int(i/s)-1 for i in g))

golden(30)
