from itertools import permutations, product

def primesets():
    for i in filter(lambda x: x[8]%2 == 1, permutations(range(1, 10), 9)):
        print(i)

#primesets()
