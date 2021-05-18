# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# create tuple
fruits = ('apples', 'oranges', 'grapes')
# fruits2 = tuple(('apples', 'oranges', 'grapes'))

# without leaving a trailing comma after a single value
# apple is seen as a string instead of a tuple
fruits2 = ('apple')
print(fruits2, type(fruits2))

fruits3 = ('apple', )
print(fruits3, type(fruits3))

# Get value
print(fruits[1])

# cannot change value!
# fruits[0] = 'Strawberries'

# delete tuple
del fruits2
# print(fruits2)

# get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set
fruits_set = {'apple', 'orange', 'banana'}

# check if something is in a set
print('apple' in fruits_set)

# add to set
fruits_set.add('grapes')
print(fruits_set)

# remove from set
fruits_set.remove('grapes')
print(fruits_set)

# clear set (empties whatever is in the set)
fruits_set.clear()
print(fruits_set)

# delete set
del fruits_set
# print(fruits_set)
