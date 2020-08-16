# program to illustrate access modifiers of a class
#Public Access Modifier:
#The members of a class that are declared public are easily accessible from any part of the program.
# All data members and member functions of a class are public by default.

#Protected Access Modifier:
#The members of a class that are declared protected are only accessible to a class derived from it.
#Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class.

#Private Access Modifier:
#The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier.
# Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class.

# super class
class Super:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member function
    def displayPublicMembers(self):
        # accessing public data members
        print("Public Data Member: ", self.var1)

    # protected member function
    def _displayProtectedMembers(self):
        # accessing protected data members
        print("Protected Data Member: ", self._var2)

    # private member function
    def __displayPrivateMembers(self):
        # accessing private data members
        print("Private Data Member: ", self.__var3)

    # public member function
    def accessPrivateMembers(self):
        # accessing private memeber function
        self.__displayPrivateMembers()

    # derived class


class Sub(Super):

    # constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    # public member function
    def accessProtectedMemebers(self):
        # accessing protected member functions of super class
        self._displayProtectedMembers()

    # creating objects of the derived class


obj = Sub("Geeks", 4, "Geeks !")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMemebers()
obj.accessPrivateMembers()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)

#output:
#Public Data Member:  Geeks
#Protected Data Member:  4
#Private Data Member:  Geeks !
#Object is accessing protected member: 4
