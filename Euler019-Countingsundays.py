def sundays():
    d = 0
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    s = 0
    for i in range(99):
        for j in range(12):
            if j == 1 and i % 4 == 0:
                d += 1
            d += m[j]
            if d % 7 == 5:
                s += 1
    print(s)

sundays()
