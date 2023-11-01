# Iterater forever
# exit with Ctrl+C

class Repeater:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return RepeaterIterater(self)
    
class RepeaterIterater:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value

# repeater = Repeater("hello")
# for item in repeater:
#     print(item)

# repeater = Repeater("Hello")
# iterator = repeater.__iter__()
# while True:
#     item = iterator.__next__()
#     print(item)

repeater = Repeater("Hello")
iterator = iter(repeater)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))