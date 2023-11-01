my_items = ['a', 'b', 'c']

i = 0
while i < len(my_items):
    print(my_items[i])
    i +=1

print(range(len(my_items)))

print(list(range(len(my_items))))

for i in range(len(my_items)):
    print(my_items[i])

for item in my_items:
    print(item)

for i, item in enumerate(my_items):
    print(f'{i}: {item}')