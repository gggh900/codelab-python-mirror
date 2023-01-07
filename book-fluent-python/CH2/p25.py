# List comprehensions and readibility.
# To compare the performance of typical classical for loop and 
# list comprehensions, refer to p25-2.py
#!/usr/bin/python3
import code
symbols="$c%="

codes=[]
for symbol in symbols:
    codes.append(ord(symbol))
    print("appending ", ord(symbol))
print(codes)

# Using listcomprehension.

codes = [ord(symbol) for symbol in symbols]
print(codes)
