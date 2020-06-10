from math import floor
def combos():
    t = 1
    for i in range(3):
        for j in range(5-(2*i)):
            for k in range(1+(floor(10-5*i-2.5*j))):
                for l in range(1+(20-10*i-5*j-2*k)):
                    for m in range(1+(40-20*i-10*j-4*k-2*l)):
                        for n in range(1+(floor(100-50*i-25*j-10*k-5*l-2.5*m))):
                            t+=1

    print(t)

combos()
