from itertools import permutations

def substring():
    t = 0
    for i in permutations('0123456789'):
        s = "".join(i)
        if s[5] == '5':
            if int(s[7:10]) % 17 == 0 and int(s[6:9]) % 13 == 0 and int(s[5:8]) % 11 == 0 and int(s[4:7]) % 7 == 0 and int(s[3:6]) % 5 == 0 and int(s[2:5]) % 3 == 0 and int(s[1:4]) % 2 == 0:
                t += int(s)
    print(t)

substring()
