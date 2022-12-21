def factorial(n):
    """returns "!"""
    return 1 if n < 2 else n*factorial(n-1)

factorial(42)
print(factorial.__doc__)
print(type(factorial))
print(dir(factorial))
print('0x'+str(id(factorial)))

fact=factorial
print(fact)
print('0x'+str(id(fact)))
fact(5)
print(map(factorial, range(11)))
print(list(map(factorial, range(11))))
