#from mirror import LookingGlass
import sys

class LookingGlass:
    def __enter__(self):
        print("LookingGlass.__enter__ entered.")
        self.original_write=sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERMOCKY'

    def reverse_write(self, text):
#        print("LookingGlass.reverse_write entered.")
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback): 
        print("LookingGlass.__exit__ entered.")

        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("Pls do not divide by 0")
            return True

with LookingGlass() as what:
    print('Alice')
    print(what)
print('back to normal')
print(what)
