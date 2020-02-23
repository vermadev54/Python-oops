"""
    # Checking error parameter using class decorator :
      This type of class decorator is most frequently used. This decorator checks parameters before executing
      the function preventing the function to become overloaded and enables it to store only logical and necessary statements.
"""

# Python program checking
# error parameter using
# class decorator

class ErrorCheck:

    def __init__(self, function):
        self.function = function

    def __call__(self, *params):
        if any([isinstance(i, str) for i in params]):
            raise TypeError("parameter cannot be a string !!")
        else:
            return self.function(*params)


@ErrorCheck
def add_numbers(*numbers):
    return sum(numbers)

if __name__ == '__main__':

    #  returns 6
    print(add_numbers(1, 2, 3))

    # raises Error.
    print(add_numbers(1, '2', 3))

"""
6
Traceback (most recent call last):
  File "class-decorator-6.py", line 33, in <module>
    print(add_numbers(1, '2', 3))
  File "class-decorator-6.py", line 18, in __call__
    raise TypeError("parameter cannot be a string !!")
TypeError: parameter cannot be a string !!

"""