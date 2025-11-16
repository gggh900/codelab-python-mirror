def deco(func):
    def inner():
        print("inner_in()...")
        func()
        print("inner_out()...")
    return inner
    
@deco
def target():
    print("running target()")

target()
