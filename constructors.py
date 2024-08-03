# 1. Class with default, one-argument, and two-argument constructors
class MyClass:
    def __init__(self, arg1=None, arg2=None):
        # Default constructor
        if arg1 is None and arg2 is None:
            print("Default constructor called")
        # One-argument constructor
        elif arg2 is None:
            self.arg1 = arg1
            print(f"One-argument constructor called with arg1={arg1}")
        # Two-argument constructor
        else:
            self.arg1 = arg1
            self.arg2 = arg2
            print(f"Two-argument constructor called with arg1={arg1} and arg2={arg2}")

# Main function to instantiate the class
def main():
    print("Creating instances of MyClass:")
    obj1 = MyClass()                  # Calls default constructor
    obj2 = MyClass(10)                # Calls one-argument constructor
    obj3 = MyClass(10, 20)            # Calls two-argument constructor

# 2. Call constructors of super class from a child class
class SuperClass:
    def __init__(self, arg1=None):
        print(f"SuperClass constructor called with arg1={arg1}")

class SubClass(SuperClass):
    def __init__(self, arg1=None, arg2=None):
        super().__init__(arg1)        # Call super class constructor
        print(f"SubClass constructor called with arg2={arg2}")

# 3. Apply access modifiers to constructors (Python does not have strict access modifiers like other languages)
class AccessModifiers:
    def __init__(self):
        print("Public constructor")

    def _protected_constructor(self):
        print("Protected constructor (by convention)")

    def __private_constructor(self):
        print("Private constructor (by name mangling)")

# 4. Illustrate the concept of attributes of a constructor
class ConstructorAttributes:
    def __init__(self, value):
        self.value = value
        print(f"Constructor called with value={value}")

    def display(self):
        print(f"Value is {self.value}")

# Main function to test the concepts
if __name__ == '__main__':
    main()                          # Test class constructors

    print("\nCreating instances of SubClass:")
    sub_obj = SubClass(10, 20)     # Calls SuperClass and SubClass constructors

    print("\nTesting AccessModifiers:")
    access_obj = AccessModifiers()  # Calls public constructor
    access_obj._protected_constructor()  # Calls protected constructor (by convention)
    access_obj._AccessModifiers__private_constructor()  # Calls private constructor (by name mangling)

    print("\nTesting ConstructorAttributes:")
    attr_obj = ConstructorAttributes(100)  # Calls constructor with attribute
    attr_obj.display()  # Displays the attribute value
