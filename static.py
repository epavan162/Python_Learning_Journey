class MyClass:
    # 1. Define a static variable
    static_variable = "Initial Value"

    @classmethod
    def access_static_variable(cls):
        return cls.static_variable

    def change_static_variable_instance(self, new_value):
        # 2. Access and change static variable through an instance
        MyClass.static_variable = new_value

    @classmethod
    def change_static_variable_class(cls, new_value):
        # 3. Change static variable within the class
        cls.static_variable = new_value
        

# 1. Access static variable through the class
print("Static Variable (Class Access):", MyClass.access_static_variable())

# Create an instance of MyClass
obj = MyClass()

# 2. Access static variable and change it through an instance
print("Access Static Variable (Instance):", obj.access_static_variable())
obj.change_static_variable_instance("Changed Value via Instance")
print("Static Variable (After Instance Change):", MyClass.access_static_variable())

# 3. Change static variable within the class
MyClass.change_static_variable_class("Changed Value via Class")
print("Static Variable (After Class Change):", MyClass.access_static_variable())
