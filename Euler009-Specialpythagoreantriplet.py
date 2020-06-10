def triplet(n):
    for i in range(3, int(n/3)):
        for j in range(int((n-i)/2)+1, i, -1):
            if i**2 + j**2 == (n-i-j)**2:
                print(i*j*(n-i-j))
                break

triplet(1000)
