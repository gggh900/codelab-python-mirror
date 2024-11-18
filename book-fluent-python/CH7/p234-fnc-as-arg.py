fruits=['grape','raspberry','apple','banana']
print(fruits)
def reverse(word):
    return word[::-1]

print(reverse('testing'))
print(sorted(fruits, key=reverse))
print(fruits)
