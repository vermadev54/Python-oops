"""
Using class Decorators to print Time required to execute a program :
In order to print time required to execute a program,
we use __call__ function and use a time module so that we can get a execute time of a program
"""

# Python program to execute
# time of a program
# importing time module

from time import time
class Timer:

	def __init__(self, func):
		self.function = func

	def __call__(self, *args, **kwargs):
		start_time = time()
		result = self.function(*args, **kwargs)
		end_time = time()
		print("Execution took {} seconds".format(end_time-start_time))
		return result


# adding a decorator to the class
@Timer
def some_function(delay):
	from time import sleep

	# Introducing some time delay to
	# simulate a time taking function.
	sleep(delay)
if __name__ == '__main__':
    some_function(3)

"""
O/P
Execution took 3.0020840167999268 seconds
"""