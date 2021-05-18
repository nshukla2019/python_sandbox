# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


name = 'Nupur'
age = 20

# Concatenate

# needed to convert age to a string to concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by position (whatever is in {} is a place holder which is formatted with .format())
print('My name is {name} and I am {age}'.format(name=name, age=age))


# F-Strings (3.6+) (inserting variables directly into string)
print(f'Hi, my name is {name} and I am {age}')


# String Methods

s = 'hello world'

# capitalization
print(s.capitalize())

# all lowercase
print(s.lower())

# all uppercase
print(s.upper())

# swaps lower with upper and upper with lower
print(s.swapcase())

# gets length of string
print(len(s))

# replaces the first arg with the second
print(s.replace('world', 'people'))

# counts the number of given character in string
print(s.count('e'))

# starts with (bool)
print(s.startswith('hello'))

# ends with (bool)
print(s.endswith('d'))

# split string into a list
print(s.split())

# finding position of a given character
print(s.find('r'))

# is all alphanumeric (bool)
print(s.isalnum())

# is all alphabetic (bool)
print(s.isalpha())

# is all numeric (bool)
print(s.isnumeric())
