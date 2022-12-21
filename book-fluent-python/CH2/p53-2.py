import math

DEFINE_IADD=0
class Vector:
    def __init__(self,x=0, y=0):
        self.x=x
        self.y=y

    def __repr__(self):
        return f'vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        print("calling __add__")
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __lt__(self, other):
        return abs(self) < abs(other)

    if (DEFINE_IADD==1):
        def __iadd__(self, other):
            print("calling __iadd__")
            #return self + other
            self.x += other.x
            self.y += other.y
            return self

a=Vector(1, 2)
b=Vector(3, 4)

a+=b
print(a)
