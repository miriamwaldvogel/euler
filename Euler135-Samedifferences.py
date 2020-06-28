def solutions(n):
    s = [0]*(n+1)
    for i in range(1, int(n/2)+1):
        for j in range(1, int(n/i)+1):
            if 3*j > i and (i+j) % 4 == 0 and (3*i-j) % 4 == 0:
                s[i*j] += 1
    print(sum(1 for i in s if i == 10))

solutions(1000000)
