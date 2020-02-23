"""
##Decorators in Python##
In Python, functions are the first class objects, which means that –
    # Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
    # for example we can pass function to other function as argument, we can return function, we can assign function to other variable.
    # Functions can be defined inside another function and can also be passed as argument to another function.
    # Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function
      or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function,
      without permanently modifying it.
    # In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

    # How does it work?
    # a) The function `decorated()` gets called.
    # b) Since the decorator `@my_decorator` is defined above
    # `decorated()`, `my_decorator()` gets called.
    # c) my_decorator() takes a function name as args, and hence `decorated()`
    # gets passed as the arg.
    # d) `my_decorator()` does it's job, and when it reaches `myfunction()`
    # calls the actual function, ie.. decorated()
    # e) Once the function `decorated()` is done, it gets back to `my_decorator()`.
    # f) Hence, using a decorator can drastically change the behavior of the
    # function you're actually executing.
"""
def my_decorator(my_function):    # <-- (4)
    def inner_decorator():        # <-- (5)
        print("This happened before!")  # <-- (6)
        my_function()             # <-- (7)
        print("This happens after ")    # <-- (10)
        print("This happened at the end!")    # <-- (11)
    return inner_decorator
    # return None


@my_decorator       # <-- (3)
def my_decorated():    # <-- (2) <-- (8)
    print("This happened!")   # <-- (9)

if __name__ == '__main__':
    my_decorated()    # <-- (1)

# This prints:
# # python 19-decorators-1.py
# This happened before!
# This happened!
# This happens after
# This happened at the end!