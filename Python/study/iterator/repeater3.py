
# def bounded_repeater(value, max_repeats):
#     count = 0
#     while True:
#         if count >= max_repeats:
#             return
#         count +=1
#         yield value

def bounded_repeater(value, max_repeats):
    for _ in range(max_repeats):
        yield value

for x in bounded_repeater('Hi', 4):
    print(x)


iterator = ('Hello' for _ in range(3))

# for x in iterator:
#     print(x)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

liter = ['Hi' for _ in range(3)]

# for x in liter:
#     print(x)

print(next(liter))