class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'

class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().ping()

class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')
        super().ping()

class Leaf(A,B):
    def ping(self):
        print(f'{self}.ping() in Lead')
        super().ping()

class U():
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()

class leafUA(U,A):
    def ping(self):
        print(f'{self}.ping() in leafUA')
        super().ping()

print("leaf1: ")
leaf1=Leaf()
print(leaf1.ping())
print(leaf1.pong())

print("leafUA: ")
leaf2 = leafUA()
print(leaf2.ping())
print(leafUA.__mro__)


