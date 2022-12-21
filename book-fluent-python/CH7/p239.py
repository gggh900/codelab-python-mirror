import random

class BingoCage:
    def __init__(self,items):
        self.__items = list(items)
        random.shuffle(self.__items)

    def pick(self):
        try:    
            return self.__items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage!')

    def __call__(self):
        return self.pick()

bingo=BingoCage(range(10))
print(bingo.pick())
print(callable(bingo))
print(bingo())
