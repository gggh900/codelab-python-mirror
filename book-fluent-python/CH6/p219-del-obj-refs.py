import weakref
s1={1,2,3}
s2=s1

# weak references

def bye():
    print("...like tears in the rain.")

ender=weakref.finalize(s1, bye)
print(ender.alive)

#s1 is pointing away from {1,2,3} now.

del s1
print(ender.alive)

#s2 is pointing away from {1,2,3} now. Nothing should be pointing.

s2='spam'
print(ender.alive)
