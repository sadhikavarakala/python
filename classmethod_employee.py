'''
method - function asscociated with a class
class variable = variables that are shared among all instances in a class
instance variable - variables that are unique to each instance of a class
'''
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
     
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 

emp_1 = Employee('Will', 'Smith', 50000) #instances of employee class
emp_2 = Employee('Rain', 'Kim', 60000)

import datetime
my_date = datetime.date(2020, 7, 10)

print(Employee.is_workday(my_date))

# class method
# emp_str_1 = 'John-Doe-90000'
# emp_str_2 = 'Steven-Smith-80000'
# emp_str_3 = 'Mary-Jane-869000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.first)
