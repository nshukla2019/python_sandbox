# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create dictionary

person = {
    'firstName': 'Nupur',
    'lastName': 'Shukla',
    'age': 20
}

# use a constructor

#person2 = dict(firstName='sara', lastName='williams')

print(person, type(person))
#print(person2, type(person2))

# get value
print(person['firstName'])

# get value
print(person.get('lastName'))


# Add key/value
person['phone'] = '123-456-7890'
print(person)

# get dictionary keys
print(person.keys())

# get dictionary items
print(person.items())

# copy dictionary
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# remove an item using del and pop
del(person['age'])
person.pop('phone')
print(person)

# clear
person.clear()
print(person)

# get length
print(len(person2))

# list of dictionaries
people = [
    {'name': 'Bob', 'age': 34},
    {'name': 'hello', 'age': 23}
]

print(people)

# getting specific info inside list of dictionaries
print(people[0]['name'])
