# Classes

class Employee:
    raise_amt = 1.05

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '@company.com'
    
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first_name, last_name, salary, prog_language):
        super().__init__(first_name, last_name, salary)
        self.prog_language = prog_language

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees = None):
        super().__init__(first_name, last_name, salary)
        if employees is  None:
            self.employees = []
        else: 
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.full_name())



emp1 = Employee('John', 'Doe', 20000)
emp2 = Employee('Sarah', 'Doe', 90000)
emp3 = Employee('Mike', 'Doe', 50000)

mgr1 = Manager('James', 'Burton', '50000', [emp1, emp2, emp3])

mgr1.add_employee(Employee('Will', 'Smith', 40000))

mgr1.remove_employee(emp2)

mgr1.print_emps()