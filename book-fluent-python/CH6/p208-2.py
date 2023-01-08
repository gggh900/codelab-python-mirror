'''
l2 creates new separate entity not alias.
Therefore l2==l1 compares value which results in true
but l2 is l1 compares the object not just value which is different.
'''
l1=[3,[55,44], (7,8,9)]
l2=list(l1)

print("l2: ", l2)
print("l2 == l1: ", l2==l1)
print("l2 is l1: ", l2 is l1)
