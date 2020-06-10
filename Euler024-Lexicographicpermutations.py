from itertools import permutations

def lexicographic(n):
    for i, j in enumerate(permutations(range(10), 10)):
        if i == n-1:
            print("".join([str(k) for k in j]))
            break

lexicographic(1000000)
