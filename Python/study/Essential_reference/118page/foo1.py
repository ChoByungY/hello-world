# import foo
from foo import callf

x = 37

def helloworld():
    return "Hello world!!     x is %d" % x

print (callf(helloworld))

def bar():
    x = 13
    def helloworld():
        return "Hello world. x is %d" % x
    print ( callf(helloworld) )

bar()