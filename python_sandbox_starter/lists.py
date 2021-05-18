# A List is a collection which is ordered and changeable. Allows duplicate members.

# creating a list

nums = [1, 2, 3, 4, 5]
fruits = ['apples', 'grapes', 'oranges', 'blueberries']

# using a constructor to create a list
#nums2 = list((1, 2, 3, 4, 5))

print(nums)


# getting a value
print(fruits[1])

# getting a length
print(len(fruits))

# append to the end of the list
fruits.append('mangos')
print(len(fruits))

# remove from list
fruits.remove('grapes')
print(len(fruits))

# inserts second arg into first arg
fruits.insert(2, 'Strawberries')
print(fruits)

# remove with pop method
fruits.pop(2)
print(fruits)


# reverse list
fruits.reverse()
print(fruits)

# sort list (alphabetically)
fruits.sort()
print(fruits)


# reverse sort
fruits.sort(reverse=True)
print(fruits)

# change a value
fruits[0] = 'yummy'
print(fruits)
