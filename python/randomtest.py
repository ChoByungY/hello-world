# This is same with next paragraph
from random import randint

items = ['a', 'b', 'c', 'd']
end = len(items) -1
r = randint(0, end)
print(items[r])

# This is same with upper paragraph
from random import choice
print(choice(items))
