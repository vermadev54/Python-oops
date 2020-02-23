"""
Class Decorator with *args and **kwargs :
In order to use class decorator with argument *args and **kwargs
we used a __call__ function and passed both the argument in a given function

"""
# Python program showing
# class decorator with *args
# and **kwargs

class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # We can add some code
        # before function call

        self.function(*args, **kwargs)

        # We can also add some code
        # after function call.


# adding decorator to the class
@MyDecorator
def function(name, message='Hello'):
    print("{}, {}".format(message, name))

if __name__ == '__main__':
    function("jainendra kumar", "hello")

"""
hello, jainendra kumar
"""