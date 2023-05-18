def print_fcn_name(func):
        def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@print_fcn_name
def f1():
    print("this is f1...")

f1()
