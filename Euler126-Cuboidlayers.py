def cubes(a, b, c, l):
    return(2*((a*b)+(b*c)+(a*c))+(4*(a+b+c+l-2)*(l-1)))

def layers(l, n):
    m = 1
    while cubes(m, 1, 1, 1) < l:
        m += 1
    m -= 1
    c = [0]*(l+1)
    for i in range(1, m+1):
        for j in range(i, int(((l/2)-i)/(i+1))+1):
            for k in range(j, int(((l/2)-(i*j))/(i+j))+1):
                o = 1
                a = cubes(i, j, k, o)
                while a < l:
                    c[a] += 1
                    o += 1
                    a = cubes(i, j, k, o)
    if n in c:
        print(c.index(n))

layers(20000, 1000)
