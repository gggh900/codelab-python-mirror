def printFnc(func):
    print("printFnc: func: ", func)
    def inner(*args):
        #print("printFcn.inner() entered")
        print("func: ", func.__name__, end= ' ')
        print("args: ", end=' ')
        for i in args[1:]:
            print(i, end=' ')
        print("\n")
        return func(*args)
    return inner


@printFnc
def f1(p1):
    print("f1: p1: ", p1)

@printFnc
def f2(p1, p2):
    print("f2: p1/p2: ", p1, p2)

f1(123)
f2(133, 11)
