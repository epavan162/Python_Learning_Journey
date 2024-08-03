from abc import ABC, abstractmethod

# 1. Create an abstract class with abstract and non-abstract methods.
class AbstractClass(ABC):

    # Abstract method
    @abstractmethod
    def abstract_method(self):
        pass

    # Non-abstract method
    def non_abstract_method(self):
        print("This is a non-abstract method in AbstractClass.")

# 2. Create a sub class for an abstract class.
class SubClass(AbstractClass):

    # Implementing the abstract method
    def abstract_method(self):
        print("This is the implementation of the abstract method in SubClass.")

    # Additional non-abstract method in SubClass
    def another_non_abstract_method(self):
        print("This is another non-abstract method in SubClass.")

# 3. Create an object in the child class for the abstract class and access the non-abstract methods.
print("Accessing methods using AbstractClass reference:")
abstract_ref = SubClass()
abstract_ref.non_abstract_method()

# 4. Create an instance for the child class in child class and call abstract methods.
print("\nAccessing abstract method using SubClass reference:")
child_instance = SubClass()
child_instance.abstract_method()

# 5. Create an instance for the child class in child class and call non-abstract methods.
print("\nAccessing non-abstract methods using SubClass reference:")
child_instance.non_abstract_method()
child_instance.another_non_abstract_method()
