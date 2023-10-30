# List

d1 = list(range(2, 10))

d2 = [ i ** 2 for i in range(10)]

print(d1, d2)

print(" ".join(str(i) for i in d1))

v1 = [list(range(10)), [10, 11, 12]]

print(v1)

print( [j for i in d1 for j in d2 if i > 5])

print( [i for i in d1 for _ in d2 if i > 5])

print([i if i > 5 else "No" for i in d1])