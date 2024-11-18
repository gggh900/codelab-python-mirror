'''
lewis is an alias for charles. Printing id (same) confirms it.
Changing lewis also changes charles.
Alex values are same but different object. Printing id (different) 
confirms it.
'''
charles={'name': 'Charles L.Dodgson', 'born': 1832}
lewis=charles
print(charles)
print(lewis)
print(lewis is charles)
print(id(charles), id(lewis))
lewis['balance']=950
print(charles)
print(lewis)

charles={'name': 'Charles L.Dodgson', 'born': 1832}
alex={'name': 'Charles L.Dodgson', 'born': 1832}
print("alex==charles:", alex==charles)
print(alex is not charles)
print(alex is charles)
print(id(alex))
