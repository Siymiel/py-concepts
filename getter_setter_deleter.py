class Employee:
    raise_amt = 1.05

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    # Getter
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first_name, self.last_name)
    
    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    # Setter
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    # Deleter
    @full_name.deleter
    def full_name(self):
        print('Delete Name!')
        self.first_name = None
        self.last_name = None

    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

emp1 = Employee('John', 'Doe', 50000)

emp1.full_name = 'Samuel Kinuthia'

print(emp1.email)