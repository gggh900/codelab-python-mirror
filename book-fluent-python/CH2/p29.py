#!/usr/bin/python3
import array

symbols="$cEye"
a=tuple(ord(symbol) for symbol in symbols)
b=array.array('I', (ord(symbol) for symbol in symbols))
print(a)
print(b)
