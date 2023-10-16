a = [ 1, 2, 3, 4, 5]

print(a)

def square(items):
    for i, x in enumerate(items):
        items[i] = x * x

square(a)

print(a)

def factor(a):
    d = 2
    while( d <= (a / 2)):
        if ((a / d) * d == a):
            return (( a / d), d)
        d = d + 1
    return ( a, 1 )

x, y = factor(1243)

print(x,y)

b = (x,y) = factor(1243)

print(b)
    