import sys
import array as arr

a=2
b=[1,2]
b1=arr.array('i',[1,2])

c={1:"a", 2: "b"}
for i in [a,b,b1,c]:
    print("printing the byte size of ", type(i))
    print(sys.getsizeof(i))
