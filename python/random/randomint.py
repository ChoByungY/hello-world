from random import randint, randrange, choice

x = range(0,100,3)
print(x)

x = randrange(0,100,3)
print(x)

x = choice(range(1,100,3))
print(x)

items = ['a', 'b', 'c', 'd', 'e']

# This is same with next paragraph
end = len(items) -1
r = randint(0, end)
print(items[r])

# This is same with upper paragraph
from random import choice
print(choice(items))
