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

'''
This will fail because U is unrelated to A, root not inherited from any class to super().ping() from U.ping() will fail.
u=U()
u.ping()
'''

leaf2=leafUA()
leaf2.ping()

print(leafUA.__mro__)
print(U.__mro__)
