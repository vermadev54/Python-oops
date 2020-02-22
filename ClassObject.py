    """
    ##class variable ##
    # A class method is a method which is bound to the class and not the object of the class.
    # It can modify a class state that would apply across all the instances of the class. 
      For example it can modify a class variable that will be applicable to all the instances.
    # shared among all instance of class.
    # are same for all instance (same value)
    # people call alternative constructor(example: from_string)
    # from_string : suppose we are getting the employee details in string format
      ("raju-kumar-7000") to create employee from string after split.
    # A class method takes cls as first parameter while a static method needs no specific parameters.
    # A class method can access or modify class state while a static method can’t access or modify it.
    # In general, static methods know nothing about class state.
      They are utility type methods that take some parameters and work upon those parameters.
      On the other hand class methods must have class as parameter.
    # We generally use class method to create factory methods. 
      Factory methods return class object ( similar to a constructor ) for different use cases.
      We generally use static methods to create utility functions.

    ## Static Method ##
    # A static method is also a method which is bound to the class and not the object of the class.
    # A static method is also a method which is bound to the class and not the object of the class.
    # We generally use static methods to create utility functions
    """
from datetime import date
class Employee:
    def __init__(self, fistname, lastname, age, pay):
        self.firstame = fistname
        self.lastname = lastname
        self.age = age
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.firstame, self.lastname)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        firstname, lastname, age, pay = emp_str.split('-')
        return cls(firstname, lastname, age, pay)

    # A class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, emp_str, year):
        firstname, lastname, pay = emp_str.split('-')
        return cls(firstname,lastname, pay, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

emp1 = Employee("jainendra", "kumar", 20, 12000)
emp2 = Employee("nirma", "devi", 10, 15000)

print(Employee.__dict__)
print(emp2.fullname())
Employee.set_raise_amt(1.05)
print(emp2.pay)
emp3 = Employee.from_string("raju-kumar-15-70000")
emp4 = Employee.fromBirthYear('pawan-kumar-17000', 1991)

print (emp1.age)
print (emp2.age)

print(emp3.fullname())
print(Employee.isAdult(22))