# Encapsulation means to preserve data in classes using methods
# Here, we're setting the 'val' attribute through 'set_val()'.
# See the next example, `encapsulation-2.py` for more info

# In this example, we have two methods, `set_val` and `get_val`.
# The first one sets the `val` value while the second one
# prints/returns the value.
class MyClass(object):

    def set_val(self, val):
        self.value = val

    def get_val(self):
        print(self.value)
        return self.value

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)

print(a.get_val())
print(b.get_val())

# Here we see how we can set values in methods without
# going through the method itself, ie.. how we can break
# encapsulation.
# NOTE: BREAKING ENCAPSULATION IS BAD.
a.set_val(10)
b.set_val(1000)
a.value = 100    # <== Overriding `set_value` directly
# <== ie..  Breaking encapsulation

a.get_val()
b.get_val()

