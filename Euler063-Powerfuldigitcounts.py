def powerdigit():
    n = 1
    for i in range(2, 10):
        b = 1
        while len(str(i**b)) == b:
            n += 1
            b += 1
    print(n)

powerdigit()
