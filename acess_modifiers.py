# Super class
class Super:
    # Public data member
    var1 = None

    # Protected data member
    _var2 = None

    # Private data member
    __var3 = None

    # Constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # Public member function
    def displayPublicMembers(self):
        # Accessing public data members
        print("Public Data Member:", self.var1)

    # Protected member function
    def _displayProtectedMembers(self):
        # Accessing protected data members
        print("Protected Data Member:", self._var2)

    # Private member function
    def __displayPrivateMembers(self):
        # Accessing private data members
        print("Private Data Member:", self.__var3)

    # Public member function
    def accessPrivateMembers(self):
        # Accessing private member function
        self.__displayPrivateMembers()

# Derived class
class Sub(Super):
    # Constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    # Public member function
    def accessProtectedMembers(self):
        # Accessing protected member functions of super class
        self._displayProtectedMembers()

# Creating objects of the derived class
obj = Sub("Pavan", 6263, "Personals")

# Calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# Object cannot access private member, so it will generate AttributeError
# Uncommenting the following line will generate an error
# print(obj.__var3)
