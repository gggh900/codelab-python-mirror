
a=[1,2]

# b is a 2nd reference to a.

b=a

# object still exists since b is pointer but a is no longer pointing to [1,2] 
# so print should be ok.

del a
print(b)

# b is reasiigned to object [1,2] should not exist. and b has no value.
b=[3]
print(b)
