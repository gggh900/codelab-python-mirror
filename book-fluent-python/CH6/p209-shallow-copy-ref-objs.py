l1=[3,[66,55,44],(7,8,9)]

# l2 is a shallow copy of l1. this means, although l2 is separate object than l1, its list/tuple members inside
# [66,55,44],(7,8,9) are referencing same object.

l2=list(l1)

# appending l1 has no effect since l2 is separate object as it was said before.

l1.append(100)

# removing 55 from l1[1] will have effect of removing both from l1 and l2 since list is referencing same object.

l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)

# Adding to lists inside l2 also affacts samely for l1.

l2[1]+=[33,22]
l2[2]+=(10,11)
print('l1:', l1)
print('l2:', l2)

