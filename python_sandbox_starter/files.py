# Python has functions for creating, reading, updating, and deleting files.

# open a file (open() actually creates it)
myFile = open('myfile.txt', 'w')

# get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I do not know')
myFile.write(' and I do not care')

myFile.close()

# append to file (mode is 'a')

myFile = open('myfile.txt', 'a')
myFile.write(' and I do not think')

myFile.close()

# reading from file

myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)