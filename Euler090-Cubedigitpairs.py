from itertools import combinations

def cubes():
    squares = ['01', '04', '06', '16', '25', '36', '46', '81']
    t = 0
    for i, j in combinations(combinations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '6'], 6), 2):
        a = [0 for k in range(8)]
        for k in i:
            for l in j:
                if k+l in squares:
                    a[squares.index(k+l)] = 1
                elif l+k in squares:
                    a[squares.index(l+k)] = 1
        if sum(a) == 8:
            t+=1
    print(t)

cubes()
