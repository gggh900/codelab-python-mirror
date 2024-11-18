# unfinished.

import time

DEFAULT_FMT='[{elapsed:0.8f}s] {name}({args}) -> {result}'

class clock:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt=fmt

    def __call__(self,func):
        def clocked(*args):
            t0 = time.perf_counter()
            result=func(*args)
            elapsed=time.perf_counter()-t0
            name=func.__name__
            arg_str=', '.join(repr(arg) for arg in args)
            print(fmt.format(**locals()))
            return result
        return clocked

@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)

@clock()
def snooze1(seconds):
    time.sleep(seconds)

for i in range(3):
    snooze(.123)
for i in range(3):
    snooze1(.123)
