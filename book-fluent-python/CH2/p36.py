#!/usr/bin/python3
import os
path, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
print(path, ':', filename)

a,b, *rest = range(5)
print(a,b, rest)
a,b, *rest = range(3)
print(a,b, rest)
a,b, *rest = range(2)
print(a,b, rest)
a, *body, c,d = range(5)
print(a, body, c, d)
*head, b,c,d = range(5)
print(head, b,c,d)
