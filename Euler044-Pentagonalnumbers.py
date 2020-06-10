def pentagonal():
    p = set()
    a = 0
    i = 1000
    while a == 0:
        i += 1
        s = int((3*i*i-i)/2)
        for j in p:
            if s-j in p and s-2*j in p:
                a = s-2*j
                print(a)
                break
        p.add(s)

pentagonal()
