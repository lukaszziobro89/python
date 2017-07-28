# Python Object-Oriented Programming
class Employee:

    num_of_employees = 0
    raise_amount = 1.04  # class variable

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = '{}.{}@company.com'.format(first_name, last_name)

        Employee.num_of_employees += 1  # adds 1 each time instance of class is created

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * Employee.raise_amount)

print('Number of employees: {}.'.format(Employee.num_of_employees))  # before creating instances of class

emp_1 = Employee('Lukasz', 'Ziobro', 5600)  # creating instance of class Employee
emp_2 = Employee('Corey', 'Schafer', 5000)  # creating instance of class Employee

print(emp_2.fullname())  # running from instance
print(Employee.fullname(emp_1))  # running directly from class
print('Initial salary for {} is {}.'.format(emp_1.fullname(), emp_1.salary))
emp_1.apply_raise()  # raise salary for emp_1
print('Salary for {} after raise is {}.'.format(emp_1.fullname(), emp_1.salary))
print(Employee.raise_amount)  # accessing variable from class
print(emp_1.raise_amount)  # accessing variable from instance (instance don't have it, but gets it from class)
print('Number of employees: {}.'.format(Employee.num_of_employees))  # after creating instances of class




