import sys
import array as arr

a=2
b=list(range(0,100))
b1=arr.array('I', range(0,100))

c={1:"a", 2: "b"}
for i in [a,b,b1,c]:
    print("printing the byte size of ", type(i))
    try:
        print("len: ", len(i))
    except Exception as msg:
        print("len: None")
    print(sys.getsizeof(i))
