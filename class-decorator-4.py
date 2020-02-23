"""
    # Class Decorator with return statement :
     In the given example the functions did not return anything so there is not any issue,
     but one may need the returned value. So we use return statement with the class decorator.
"""


# Python program showing
# class decorator with
# return satement

class SquareDecorator:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # before function
        result = self.function(*args, **kwargs)
        print(result)
        # after function
        return result

        # adding decorator to the class


@SquareDecorator
def get_square(n):
    print("given number is:", n)
    return n * n

if __name__ == '__main__':
    print("Square of number is:", get_square(195))

"""
given number is: 195
38025
Square of number is: 38025
"""