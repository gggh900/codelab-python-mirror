''' dictionary comprehension
'''
#!/usr/bin/python3

dial_codes=[
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86,'China'),
    (91,'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
]

country_dial = {country: code for code, country in dial_codes}
print(country_dial)
