def cancel():
    f = []
    n = 1
    d = 1
    for i in range(12, 99):
        a = str(i)[0]
        b = str(i)[1]
        if b != '0':
            for j in range(1, int(a)):
                p = int(str(j)+a)
                if i/p > 1 and i/p == int(b)/j:
                    f.append(int(b))
                    f.append(j)
            for j in range(1, int(b)):
                p = int(b+str(j))
                if i/p > 1 and i/p == int(a)/j:
                    f.append(int(a))
                    f.append(j)
    for i in range(0, 8, 2):
        n*=f[i]
        d*=f[i+1]
    print(int(n/d))

cancel()
