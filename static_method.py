# Static Method: This is rather simple, it's not bound to instance or class and you can simply call that using class name.

class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# So let's say in above example you need a validation that first_name should not exceed 20 characters, you can simply do this.
        
@staticmethod  
def validate_name(name):
    return len(name) <= 20

# and you could simply call using class name

Person.validate_name("Samuel Kinuthia") # Note - we don't need to create a new instance for the Person class - we directly call the validate_name method on the class itself.


# Summary Notes:
# --------------------------------------------------------------------
# Simple functions with no self argument.
# Work on class attributes; not on instance attributes.
# Can be called through both class and instance.
# The built-in function staticmethod()is used to create them.

# Benefits of Static Methods:
# --------------------------------------------------------------------
# It localizes the function name in the classscope
# It moves the function code closer to where it is used
# More convenient to import versus module-level functions since each method does not have to be specially imported

# A static method in programming refers to a method that belongs to a class rather than an instance of the class.