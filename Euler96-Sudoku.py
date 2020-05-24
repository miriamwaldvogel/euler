f = open('/mnt/chromeos/MyFiles/Downloads/Euler problems/p096_sudoku.txt', 'r')
g = f.readlines()
f.close()
h = ''.join(i[:9] for i in g if 'Grid' not in i)
h = [h[i:i+81] for i in range(0, len(h), 81)]
t = 0
def row(a, b):
    if int(a/9) == int(b/9):
        return(True)
    else:
        return(False)

def col(a, b):
    if (a-b) % 9 == 0:
        return(True)
    else:
        return(False)

def square(a, b):
    if int(a/27) == int(b/27) and int((a%9)/3) == (int(b%9)/3):
        return(True)
    else:
        return(False)

def sudoku(n):
    global t
    a = n.find('0')
    if a == -1:
        t+=int(n[:3])
    e = set()
    for i in range(81):
        if row(a, i) or col(a, i) or square(a, i):
            e.add(n[i])
    for j in '123456789':
        if j not in e:
            sudoku(n[:a]+j+n[a+1:])

for i in h:
    sudoku(i)
print(t)
