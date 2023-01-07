''' 1st example, x remains as ABC.
2nd exanple: beause of walrus assignment := x keeps defined even though 
it is only used inside list comprehensions.
3rd example: c is not defined as it is only used inside list comprehension
and out of scope outside that.
'''
x='ABC'
codes = [ord(x) for x in x]
print(codes)
print(x)

print('-'*50)
x='ABC'
codes = [last := ord(x) for x in x]
print(codes)
print(last)
print('-'*50)
x='ABC'
codes = [ord(c) for c in x]
print(codes)
try :
    print(c)
except Exception as msg:
    print(msg)
