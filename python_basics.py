# 1. Write a program to print your name.
print("Pavan Kalyan")

# 2. Write a program for a Single line comment and multi-line comments
# Single line comment in Python
"""
It is Docstring, it is not correct way to write Multi-line comment in Python
"""

# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
# Integer
integer_var = 10
# Boolean
boolean_var = True
# Character
char_var = 'A'
# Float
float_var = 10.5
# Double (in Python, float is used for double precision)
double_var = 20.123456789

print("Integer:", integer_var)
print("Boolean:", boolean_var)
print("Character:", char_var)
print("Float:", float_var)
print("Double:", double_var)

# 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables
# Global variable
variable = "Global"

def my_function():
    # Local variable with the same name
    variable = "Local"
    print("Inside function, variable:", variable)

my_function()
print("Outside function, variable:", variable)
