from math import sqrt

def solutions(m, b):
    a = (-2*m*b+sqrt(4*m*m*b*b-4*(4+m*m)*(b*b-100)))/(8+2*m*m)
    c = (-2*m*b-sqrt(4*m*m*b*b-4*(4+m*m)*(b*b-100)))/(8+2*m*m)
    return((a, m*a+b), (c, m*c+b))

def reflect(m, x, y):
    b = m
    a = y/(4*x)
    s = (pow(a, 2) * b + 2*a - b) / (1 + 2*a*b - pow(a, 2))
    return(s, y-s*x)

r = reflect(-197/14, 1.4, -9.6)
x = 1.4
y = -9.6
i = 0
while y < 9 or x > 0.01 or x < -0.01:
    s = solutions(r[0], r[1])
    if abs(x-s[0][0])<abs(x-s[1][0]):
        x = s[1][0]
        y = s[1][1]
    else:
        x = s[0][0]
        y = s[0][1]
    r = reflect(r[0], x, y, i)
    i += 1
print(i, x, y)
