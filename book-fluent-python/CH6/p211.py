''' another example of deep vs shallow copy.
bus2: shallow copy, as a result, when you drop bill from bus1, bus2 gets affected 
because passengers member is pointing to same object.
bus3 is not affected because it made deep copy meaning object members i.e.
passengers has been made a separate copy.
'''
import copy
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers=[]
        else:
            self.passengers=list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1=Bus(['Alice','Bill','Claire','David'])
bus2=copy.copy(bus1)
bus3=copy.deepcopy(bus1)

print(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')
print(bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)
