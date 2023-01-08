''' 
Example of function changing the mutable vs. immutable object 
on return
'''

def f(a,b):
    a+=b
    return a

# x is changed. 

x=1
y=2
print(f(x,y))
print(x,y)

# a is changed.

a=[1,2]
b=[3,4]
print(f(a,b))
print(a,b)

# t is not changed. 

t=(10,20)
u=(30,40)
print(f(t,u))
print(t,u)



