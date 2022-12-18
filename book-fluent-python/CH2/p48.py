#!/usr/bin/python3

# when slicing is used with 3 parameters s[a:b:c], c specifies stride.
s='bicycle'

for i in range(10, 1, -1):
    print("slice stride: ", i)
    print(s[::i])
