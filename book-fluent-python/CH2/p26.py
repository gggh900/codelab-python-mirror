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
