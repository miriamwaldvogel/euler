def sumdigits(n):
    return(sum(int(i) for i in str(n)))

def a(n):
    b = []
    for i in range(2, 100):
        for j in range(2, 10):
            if sumdigits(i**j) == i:
                b.append(i**j)
    print(sorted(b)[n-1])

a(30)
