def pandigitalprime(n):
    isprime = [True]*(n+1)
    p = 2
    d = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while p*p <= n:
        if isprime[p]:
            for i in range(2*p, n+1, p):
                isprime[i] = False
        p+=1
    isprime[0] = False
    isprime[1] = False
    for i in range(n, -1, -1):
        if isprime[i] and sorted([j for j in str(i)]) == d[:len(str(i))]:
            print(i)
            break

pandigitalprime(9999999)
