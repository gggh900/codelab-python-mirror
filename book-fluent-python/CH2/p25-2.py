# List comprehensions and readibility.

#!/usr/bin/python3
import code
import time 
symbols="$c%="
symbols="c" * 100000
codes=[]

t1=time.perf_counter()
for symbol in symbols:
    codes.append(ord(symbol))
#print(codes)
t2=time.perf_counter()
print(f'Elapsed time: {t2-t1}')

# Using listcomprehension.

t1=time.perf_counter()
codes = [ord(symbol) for symbol in symbols]
#print(codes)
t2=time.perf_counter()
print(f'Elapsed time: {t2-t1}')
