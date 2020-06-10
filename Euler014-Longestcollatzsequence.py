def longestcollatz(n):
    c = 0
    a = 2
    b = 0
    for i in range(500001, 600000, 2):
        a = 2
        b = i
        while b != 1:
            if b%2==0:
                b/=2
            else:
                b = (3*b)+1
                b/=2
            a +=1
        if a >= c:
            c = a
    print(c)

longestcollatz(1000000)
