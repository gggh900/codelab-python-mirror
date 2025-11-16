def deco(func):
    def inner(p1a):
        print("inner_in()...")
        print("arg: ", p1a)
        func(p1a)
        print("inner_out()...")
    return inner
    
@deco
def target(p1):
    print("running target()")

target(100)
