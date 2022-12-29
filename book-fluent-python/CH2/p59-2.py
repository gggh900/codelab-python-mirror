import sys
import array as arr 

a=[1,2,3] 
a1=[1,2,3,4] 
a2=[1,2,3,4,5] 
b=arr.array('I',[1,2,3])
b1=arr.array('I',[1,2,3,4])
b2=arr.array('I',[1,2,3,4,5])

for i in [a,a1,a2, b, b1, b2]:
    print("printing the byte size of ", type(i))
    print(sys.getsizeof(i))

