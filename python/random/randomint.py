from random import randint

items = ['a', 'b', 'c', 'd', 'e']

# This is same with next paragraph
end = len(items) -1
r = randint(0, end)
print(items[r])

# This is same with upper paragraph
from random import choice
print(choice(items))
