from math import sqrt, gcd

def torricelli(n):
    p = [[] for i in range(n+1)]
    t = set()
    for i in range(1, int(sqrt(n))+1):
        for j in range(1, i):
            if gcd(i, j) != 1:
                continue
            if (i-j) % 3 == 0:
                continue
            a = 2*i*j+j*j
            b = i*i-j*j
            if a+b > n:
                break
            for k in range(1, int(n/(a+b))+1):
                c = k*a
                d = k*b
                p[c].append(d)
                p[d].append(c)
                if len(p[c]) > len(p[d]):
                    e = p[c]
                    f = p[d]
                else:
                    e = p[d]
                    f = p[c]
                for l in f:
                    if l in e:
                        if l+c+d < n:
                            t.add(l+c+d)
    print(sum(t))

torricelli(120000)
