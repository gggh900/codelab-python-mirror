import time

DEFAULT_FMT='[elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*args):
            t0 = time.perf_counter()
            result=func(*args)
            elapsed=time.perf_counter()-t0
            name=func.__name__
            arg_str=', '.join(repr(arg) for arg in args)
            print(f'[{elapsed:0.8f}s] {name}({arg_str})->{result!r}')
            return result
        return clocked
    return decorate

@clock
def snooze(seconds):
    time.sleep(seconds)

def main():
    print('*' * 40, 'Calling snooze(.123)')
    for i in range(3):
        snooze(.123)

if __name__ == '__main__':
    main()

