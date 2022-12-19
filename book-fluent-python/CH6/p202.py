#!/usr/bin/python3

a_list=[1,2,3]
a_int=1
a_tuple=(1,2,3)
a_float=1.110
a_str="1111"
field_width=30
for obj in (a_list, a_int, a_tuple, a_float, a_str):
    print("-" * 50)
    print(f'{"object before mod":30}', type(obj), id(obj), obj)
    obj2=obj
    
    if type(obj)==str:
        obj += "2222"

    if type(obj)==int:
        obj+= 100

    if type(obj)==float:
        obj+1.3122

    if type(obj)==tuple:
        obj += (1,100)
    
    if type(obj)==list:
        obj.append(100)
    print(f'{"obj after mod":30}', type(obj), id(obj), obj)
    print(f'{"obj2":30}', type(obj2), id(obj2), obj2)

