def divisors(n):
    l = 45000
    d = [0]*l
    for i in range(1, l):
        for j in range(i, l, i):
            d[j]+= 1
        if i % 2 == 0:
            c = d[i-1] * d[int(i/2)]
        else:
            c = d[int((i-1)/2)] * d[i]
        if c > n:
            print(i*(i-1)//2)
            break

divisors(500)
