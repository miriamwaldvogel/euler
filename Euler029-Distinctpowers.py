def distinctpowers(a, b):
    p = set()
    for i in range(a, b+1):
        for j in range(a, b+1):
            p.add(i**j)
    print(len(p))

distinctpowers(2, 100)
