'''
nested unpacking example.
'''
#!/usr/bin/python3

metro_areas=[
    ('Tokyo', 'JP', 36.933, (35.689, 139.69)),
    ('Delhi', 'IN', 21.935, (28.613, 77.308)),
    ('Mexico city', 'MX', 20.142, (19.433, -99.1333)),
    ('New York-Newark', 'US', 20.104, (40.80, -74.02)),
    ('Sao Paolo', 'BR', 19.649, (-23.54, -46.63)),
]


print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
for name, _, _, (lat, lon) in metro_areas:
#   print("interim: ", name, lat, lon)
    if lon <= 0:
        print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


