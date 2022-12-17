registry=[]

def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

@register
def f3():
    print('running f3()')

print('running main()')
print('registry ->', registry)
f1()
f2()
f3()

