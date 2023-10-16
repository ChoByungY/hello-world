import foo

x = 37

def helloworld():
    return "Hello world!!     x is %d" % x

print (foo.callf(helloworld))

def bar():
    x = 13
    def helloworld():
        return "Hello world. x is %d" % x
    print ( foo.callf(helloworld) )

bar()