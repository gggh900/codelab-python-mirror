# by changing t1[-1], t1[-1] itself being mutable, its id remain unchanged and remained same object.
# so does t1 which was not assigned, only its member (list) has changed to remained same object.

# t1 is mutable but t1[-1] is not mutable.

t1=(1,2,[30,40])

#  build t2 whose items are equal to those of t1.

t2=(1,2,[30,40])

# modify t1[-1] list in place.

print("t1==t2:", t1==t2)

# identity of t1[-1] has not changed, only its value.

print("id(t1[-1]:", id(t1[-1]))
t1[-1].append(99)
print(t1)
print("id(t1[-1]:", id(t1[-1]))

# t1 and t2 is not different.

print("t1==t2:", t1==t2)

