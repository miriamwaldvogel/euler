def choose(a, b):
    t = 1
    for i in range(b+1, a+1):
        t *= i
    for i in range(2, a-b+1):
        t /= i
    return(int(t))

def combos():
    t = 0
    for i in range(101):
        for j in range(i+1):
            if choose(i, j) > 1000000:
                t +=1
    print(t)

combos()
