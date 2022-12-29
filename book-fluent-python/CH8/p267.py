class T1: 
    def __init__(self):
        print("T1 init...")
class T2(T1):
    def __init__(self):
        print("T2 init...")

    def T2():
        print("T2.T2 entered.")

def f1(p: T1) -> None:
    print("f1: entered...")

def f2(p: T2) -> None:
    print("f2: entered...")
    T2.T2()

o2=T2()
f1(o2)
o1=T1()
f2(o1)

def f3(p: Any)->None:
    print("f2: entered.")

o0=object()
o1=T1()
o2-T2()

f3(o0)
f3(o1)
f3(o2)

def f4():
    print("f4 entered.")

o4=f4()
f1(o4)
f2(o4)
f3(o4)

