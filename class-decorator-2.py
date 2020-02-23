"""
# Decorators are a very powerful and useful tool in Python since it allows programmers to modify
  the behaviour of function or class. Decorators allow us to wrap another function in order to extend
  the behaviour of the wrapped function, without permanently modifying it.

# We can define a decorator as a class in order to do that, we have to use a __call__ method of classes.
  When a user needs to create an object that acts as a function then function decorator needs
  to return an object that acts like a function, so __call__ can be useful. For Example
"""


# Python program showing
# use of __call__() method

class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        # We can add some code
        # before function call

        self.function()

        # We can also add some code
        # after function call.


# adding decorator to the class
@MyDecorator
def function():
    print("hello how are you !")

if __name__ == '__main__':
    function()

"""
O/P
hello how are you !
"""