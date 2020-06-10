def cube(n):
    m = float('Inf')
    i = 100
    cubes = {}
    s = ''
    while m == float('Inf') or len(s) <= len(str(m)):
        c = i*i*i
        s = ''.join(sorted(str(c)))
        if s in cubes:
            cubes[s] += [c]
            if len(cubes[s]) == n:
                m = min(m, cubes[s][0])
        else:
            cubes[s] = [c]
        i += 1

    print(m)

cube(5)
