# Chapter 4. More Control Flow Tools
# 4.2 for Statements

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]: # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

print(words)

# 4.3 The range() Function

for i in range(5):
    print(i)

print(range(5,10))
print(range(0,10,3))
print(range(-10,-100,-30))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
print(range(10))
print(list(range(5)))