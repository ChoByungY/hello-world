# Python tutorial, Release 3.7.0
# Chapter 3. An Informal Introduction to Python
#   3.2 First Steps Towards Programming

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
print()
