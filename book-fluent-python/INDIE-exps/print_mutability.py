#!/usr/bin/python3

# Good explanation:
# https://www.mygreatlearning.com/blog/understanding-mutable-and-immutable-in-python/#:~:text=Mutable%20is%20a%20fancy%20way,once%20it%20has%20been%20created.

a_list=[1,2,3]
a_int=1
a_tuple=(1,2,3)
a_float=1.110
a_str="1111"
a_dict={1: 300}
field_width=30
mutable_list=[]
immutable_list=[]

for obj in (a_list, a_int, a_tuple, a_float, a_str, a_dict):
    print("-" * 50)
    print(f'{"obj before mod":30}', type(obj), id(obj), obj)
    objAddrInit=id(obj)
    obj2=obj

    if type(obj)==str:
        obj += "2222"

    if type(obj)==int:
        obj+= 100

    if type(obj)==float:
        obj+=1.3122

    if type(obj)==tuple:
        obj += (1,100)
    
    if type(obj)==list:
        obj.append(100)

    if type(obj)==dict:
        obj[2]=400

    print(f'{"obj after mod":30}', type(obj), id(obj), obj)
    print(f'{"obj2":30}', type(obj2), id(obj2), obj2)

    if id(obj) == objAddrInit:
        print("Obj is mutable.")
        mutable_list.append(type(obj))
    else:
        print("Obj is immutable.")
        immutable_list.append(type(obj))

print("-" * 50)
print(f'mutable objs:30', mutable_list)
print(f'immutable objs:30', immutable_list)

