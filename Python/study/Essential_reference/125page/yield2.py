def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        g.__next__()
        return g
    return start

@coroutine
def receiver():
    print("Ready to receive")
    while True:
        n = (yield)
        print("Got %s" % n)

r = receiver()
r.send(1)
r.send(2)
r.send("Hello")