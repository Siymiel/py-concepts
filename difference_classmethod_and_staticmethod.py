# The difference occurs when there is inheritance.

# Suppose that there are two classes -- Parent and Child. If one wants to use @staticmethod, print_name method should be written twice because the name of the class should be written in the print line.

class Parent:
   _class_name = "Parent"

   @staticmethod
   def print_name():
       print(Parent._class_name)


class Child(Parent):
   _class_name = "Child"

   @staticmethod
   def print_name():
       print(Child._class_name)


Parent.print_name()
Child.print_name()

# However, for @classmethod, it is not required to write print_name method twice.

class Parent:
    _class_name = "Parent"

    @classmethod
    def print_name(cls):
        print(cls._class_name)


class Child(Parent):
    _class_name = "Child"


Parent.print_name()
Child.print_name()