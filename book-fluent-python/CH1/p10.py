# vector class implementation with special methods.
# special methods allow class to be used with standard arithmetic operations.
# For example __add__ implementation allows to add two vector classes.
# Set CONFIG_ENABLE_ADD_METHOD to 0 and see what happens.

CONFIG_ENABLE_ADD_METHOD=1
import math

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

    if CONFIG_ENABLE_ADD_METHOD:
        def __add__(self, other):
            x=self.x+other.x
            y=self.y+other.y
            return Vector(x,y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __iadd__(self, other):
        return self +  other

#    def __gt___(self, other):
#        return abs(self) < abs(other)

v1=Vector(2,4)
v2=Vector(2,1)
print(v1+v2)

v=Vector(3,4)
print(abs(v))

print(v*3)
print(abs(v*3))

print(str(v))

print(type(v))
print(type(str(v)))

print(v1 < v2)
print(v1 > v2)

print(v1 == v2)

