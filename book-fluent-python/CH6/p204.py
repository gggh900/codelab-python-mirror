charles={'name': 'Charles L.Dodgson', 'born': 1832}
lewis=charles
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
