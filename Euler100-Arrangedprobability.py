def arrangedprobability(n):
    a = 15
    b = 3
    while a < n:
        c = a
        a = 6*a-b-2
        b = c
    print(b)

arrangedprobability(1000000000000)
