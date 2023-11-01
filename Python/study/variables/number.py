#Sample variable test file are like this
print("Variable numbers test")

x = 1
y = 2.8
z = 3 + 2j

print(x,y,z)
print(type(x), type(y), type(z))

MyVariable = 100 + 300
print(MyVariable - 400)

a, *b, c = 'My project'
print(a, b, c)

d = set(b)
print(d)

from decimal import Decimal

data = list(map(Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
print(data)
print(max(data))
print(sorted(data))

a,b,c = data[:3]
print(str(a))
print(float(a))