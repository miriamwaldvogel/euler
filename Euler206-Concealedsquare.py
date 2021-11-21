def concealedsquare():
    a = 1010101010
    b = 1389026623
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(a, b, 10):
        sq = str(int(i**2))
        end = True
        for j, k in enumerate(digits):
            if sq[j*2] != k:
                end = False
                break
        if end:
            return(i)

print(concealedsquare())
