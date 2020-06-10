def largestprime(n):
    i = 2
    while i*i < n:
        if n % i == 0:
            n /= i
        i+=1
    print(int(n))

largestprime(600851475143)
