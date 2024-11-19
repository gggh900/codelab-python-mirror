import abc

class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.

        This method should raise 'lookupError' when instance is empty.
        """

    def loaded(self):
        """Return true if there's at least 1 item, 'False' otherwise."""

        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""

        items=[]
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break

        self.load(items)
        return tuple(items)

class BingoCage(Tombola):
    def __init__(self, items):
        self.__randomizer = random.SystemRandom()
        self.__items = []
        self.load(items)

    def load(self, items):
        self.__items.extend(items)
        self.__randomizer.shuffle(self.__items)

    def pick(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


