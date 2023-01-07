
fruits=['grape','raspberry','apple','banana']

# print original list

print(fruits)

# print sorted version of fruits but fruts are unchanged.

print(sorted(fruits, key=len, reverse=True))
print(fruits)

# permanently sort fruits. 

print(fruits.sort())
print(fruits)
