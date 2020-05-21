def numrectangles(a, b):
    return((((a**2)+a)*((b**2)+b))/4)

def mindiff(n):
    m = n
    b = 0
    c = 0
    for i in range(2, 100):
        for j in range(i, 100):
            a = numrectangles(i, j)
            if abs(n-a) < m:
                m = abs(n-a)
                b = i
                c = j
    print(b*c)

mindiff(2000000)
