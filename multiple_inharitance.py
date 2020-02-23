"""
Different forms of Inheritance:
1. Single inheritance: When a child class inherits from only one parent class, it is called as single inheritance. We saw an example above.

2. Multiple inheritance: When a child class inherits from multiple parent classes, it is called as multiple inheritance.
Unlike Java and like C++, Python supports multiple inheritance. We specify all parent classes as comma separated list in bracket.
"""

# Python example to show working of multiple
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print ("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print ("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print ("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()

"""
O/P
Base1
Base2
Derived
Geek1 Geek2
"""