def palindromes(n):
    t = 0
    for i in range(1, n, 2):
        a = str(bin(i))[2:]
        if a == a[::-1] and str(i) == str(i)[::-1]:
            t += i
    print(t)

palindromes(1000000)
