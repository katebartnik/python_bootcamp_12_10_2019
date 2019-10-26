
a = 10

def foo():

    def bar():
        print("Jestem funkcją wewnetrzna")

    bar()
    global a
    a = 1
    print(a)

foo()

def square(x):
    return x**2

sq = lambda x: x**2
print(sq(4))

def drugi(x):
    return int(x[1])

x = ["c1", "b2", "a3"]
print(sorted(x, key=drugi))
print(sorted(x, key=lambda x: int(x[1])))