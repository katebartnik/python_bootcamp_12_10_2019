
dane = (1, 2, 3, 4, 5)

def sumator(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)
    return sum(args)

print(sumator())
print(sumator(1))
print(sumator(1, 10, 1000))

print(sumator(*dane))
print(sumator(1, 2, 3, 4, 5))
print(sumator(1, 2, 3, a=1, b=2))
