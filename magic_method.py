"""
str() is used for creating output for end user while repr() is mainly used for debugging and development.
repr’s goal is to be unambiguous and str’s is to be readable

As seen below, __repr__ is invoked, when object is inspected in interpreter session.
On a high level, __str__ is used for creating output for end user while __repr__ is mainly used for debugging and development.
repr’s goal is to be unambiguous and str’s is to be readable.

"""

"""
Python has a set of built-in methods and __call__ is one of them.
The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
When the instance is called as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).

Note that callable() function returns True if the object appears callable,
it’s possible that it returns True even if the object is not callable. However,
if this function returns False then the object is definitely not callable.

"""
#__call__
class Person:
    i = 0

    def __init__(self, id):
        self.i = id


p = Person(10)
print('Person Class is callable = ', callable(Person))
print('Person object is callable = ', callable(p))


class Employee:
    id = 0
    name = ""

    def __init__(self, i, n):
        self.id = i
        self.name = n

    def __call__(self, *args, **kwargs):
        print('printing args')
        print(*args)

        print('printing kwargs')
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))


e = Employee(10, 'Pankaj')  # creating object

print(e)  # printing object

print(callable(e))

if callable(e):
    e()  # object called as a function, no arguments

    e(10, 20)  # only args
    e.__call__(10, 20)

    e(10, 20, {'x': 1, 'y': 2})  # only args of different types

    e(10, 'A', name='Pankaj', id=20)  # args and kwargs both


"""
Iteration: __getitem__ , __setitem__ , __len__
Python built-in types list, str, and bytes can use the slicing operator [] to access range of elements.
Implementing __getitem__, __setitem__in a class allows its instances to use the [] (indexer) operator.
Therefore, the __getitem__ and __setitem__dunder methods is used for list indexing, dictionary lookups, or accessing ranges of values.
To grasp the concept better, let’s consider the example in which we create our own custom list.
"""

import random as ran


class CustomList:
    def __init__(self, num):
        self.my_list = [ran.randrange(1, 101, 1) for _ in range(num)]

    def __str__(self):
        return str(self.my_list)

    def __setitem__(self, index, value):
        self.my_list[index] = value

    def __getitem__(self, index):
        return self.my_list[index]

    def __len__(self):
        return len(self.my_list)
obj = CustomList(5)
print(obj)
len(obj)
obj[1]
for item in obj:
    print (item)