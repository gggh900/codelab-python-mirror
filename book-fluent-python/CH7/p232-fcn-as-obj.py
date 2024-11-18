def factorial(n):
    """returns "!"""
    return 1 if n < 2 else n*factorial(n-1)

factorial(42)
print(factorial.__doc__)
print(type(factorial))
print(dir(factorial))
