# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core module
import datetime
from datetime import date
import time 
from time import time

# custom module
from validator import validate_email 

today = datetime.date.today()

today = date.today()
print(today)

timestamp = time()
print(timestamp)

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')
