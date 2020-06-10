def multiples(n):
    t = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            t += i
    print(t)

multiples(1000)
