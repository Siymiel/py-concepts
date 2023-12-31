# Class Method: Python unlike Java and C++ does not have constructor overloading. And so to achieve this you could use classmethod. Following example will explain this

# Let's consider we have a Person class which takes two arguments first_name and last_name and creates the instance of Person.

class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# Now, if the requirement comes where you need to create a class using a single name only, just a first_name, you can't do something like this in Python.

# This will give you an error when you will try to create an object (instance).
        
class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __init__(self, first_name):
        self.first_name = first_name

# However, you could achieve the same thing using @classmethod as mentioned below
        
class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def get_person(cls, first_name):
        return cls(first_name, "")
    
# NOTE: @classmethod are mostly considered as alternative constructors