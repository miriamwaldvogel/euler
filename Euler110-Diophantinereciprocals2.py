def product(n):
    p = 1
    for i in n:
        p*=i
    return(p)

def reciprocals(n):
    #2^2, 3^2 ,5, 7, 11, 13
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    t = []
    for i in range(3, 4):
        for j in range(3, 4):
            for k in range(2, 3):
                for l in range(2, 3):
                    p = [(2*i)+1, (2*j)+1, (2*k)+1, (2*l)+1]+[1 for i in range(len(primes)-4)]
                    m = 4
                    while product(p) < n:
                        #print(p)
                        p[m]+=2
                        m+=1
                    a = 1
                    for m, o in enumerate(p):
                        a*=(primes[m]**int((o-1)/2))
                    t.append(a)
    print(min(t))


reciprocals(4000000)
