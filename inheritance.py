class A:
    def display(self):
        print("Display Inside class A")
    
    def show(self):
        print("Show Inside class A")
    
    def method1(self):
        print("Method1 Inside class A")

class B(A):
    def print(self):
        print("Print Inside class B")
    
    def show(self):
        print("Show Inside class B")
    
    def method2(self):
        print("Method2 Inside class B")

class C(B):
    def show(self):
        print("Show Inside class C")

    def method3(self):
        print("Method3 Inside class C")

# Driver code
def main():
    # Instances
    a = A()
    b = B()
    c = C()
    
    # Calling methods using instances
    print("Using instance of A:")
    a.display()
    a.show()
    a.method1()

    print("\nUsing instance of B:")
    b.print()
    b.show()
    b.method2()

    print("\nUsing instance of C:")
    c.show()
    c.method3()
    
    # Calling overridden method with superclass reference
    print("\nCalling overridden method with superclass references:")
    a_ref_b = b
    a_ref_c = c
    print("Using reference of A to call method of B:")
    a_ref_b.show()  # Calls B's overridden method
    print("Using reference of A to call method of C:")
    a_ref_c.show()  # Calls C's overridden method

if __name__ == "__main__":
    main()
