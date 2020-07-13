from baseconvert import base
from math import log


def pascal(n):
    t = 0
    p = 1
    j = int(log(n, 7))
    for i in base(n, 10, 7):
        t += int((i*(i+1))/2)*p*(28**j)
        j -= 1
        p *= (i+1)
    print(t)

pascal(1000000000)
