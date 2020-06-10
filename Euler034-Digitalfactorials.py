def factorialsum():
    f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    t = 0
    for i in range(10, 99999):
        s = 0
        for j in str(i):
            n = int(j)
            s+=f[n]
        if s == i:
            t += s
    print(t)

factorialsum()
