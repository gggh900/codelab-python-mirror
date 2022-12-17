import functools

def myfunc(a, b=2):
    print(' Called myfunc with: ', (a,b))

def show_details(name, f, is_partial=False):
    print('{}'.format(name))
    print(' object: ', f)
    if not is_partial:
        print(' __name:', f.__name__)
    if is_partial:
        print('     func: ', f.func)
        print('     args: ', f.args)
        print('     keywords:', f.keywords)

    return

myfunc('a', 3)
print()

p1=functools.partial(myfunc, b=4)
show_details('partial with named default', p1, True)
p1('passing a')
p1('override b', b=5)

p2=functools.partial(myfunc, 'default a', b=99)
show_details('partial with default', p2, True)
p2()
p2(b='override b')
print()
