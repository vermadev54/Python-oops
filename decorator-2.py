"""
# An updated version of decorators-1.py
# This code snippet takes the previous example, and add a bit more information
# to the output.

"""
import datetime


def my_decorator(inner):
    def inner_decorator():
        print(datetime.datetime.utcnow())
        inner()
        print(datetime.datetime.utcnow())
    return inner_decorator


@my_decorator
def decorated():
    print("This happened!")


if __name__ == "__main__":
    decorated()

"""
# This will print: (NOTE: The time will change of course :P)
2020-02-23 04:08:12.321737
This happened!
2020-02-23 04:08:12.321737
"""