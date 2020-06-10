def paths(a, b):
    p = 1
    for i in range(a+1, a+b+1):
        p *= i
    for i in range(1, b+1):
        p /= i
    print(int(p))

paths(20, 20)
