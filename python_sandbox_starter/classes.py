# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# extend class
class Customer(User):
    # constructor
        def __init__(self, name, email, age):
            self.name = name
            self.email = email
            self.age = age
            self.balance = 0

        def setBalance(self, balance):
            self.balance = balance

        def greeting(self):
            return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# init user object
brad = User('Nupur Shukla', 'nupur@gmail.com', 20)
customer = Customer('John Doe', 'john@gmail.com', 23)
customer.setBalance(15)

# accessing methods in parent class
#print(customer.greeting())

print(customer.greeting())

brad.has_birthday()
print(brad.greeting())

