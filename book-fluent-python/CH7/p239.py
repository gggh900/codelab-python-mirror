''' Callable function example.
By implementing __call__ special method in the BingoCage class
you can call it like a funcion To see it as a proof, enable
CONFIG_DISABLE_CALL to undefine __call__ in which case
bingo() will fail.
'''
import random

CONFIG_DISABLE_CALL=1

class BingoCage:
    def __init__(self,items):
        self.__items = list(items)
        random.shuffle(self.__items)

    def pick(self):
        try:    
            return self.__items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage!')

    if not CONFIG_DISABLE_CALL:
        def __call__(self):
            return self.pick()

bingo=BingoCage(range(10))
print(bingo.pick())
print(callable(bingo))
print(bingo())
