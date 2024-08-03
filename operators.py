# 1. Write a function for arithmetic operators (+, -, *, /)
def arithmetic_operators(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Undefined (division by zero)"
    
    return addition, subtraction, multiplication, division

a = 10
b = 5
add, sub, mul, div = arithmetic_operators(a, b)
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")

# 2. Write a method for increment and decrement operators (++, --)
def increment_decrement(value):
    incremented = value + 1
    decremented = value - 1
    return incremented, decremented

value = 10
inc, dec = increment_decrement(value)
print(f"Incremented: {inc}")
print(f"Decremented: {dec}")

# 3. Write a program to find if two numbers are equal or not.
def check_equal(a, b):
    return a == b

num1 = 10
num2 = 5
result = check_equal(num1, num2)
print(f"Numbers are equal: {result}")

# 4. Program for relational operators (<, <=, >, >=)
def relational_operators(a, b):
    less_than = a < b
    less_equal = a <= b
    greater_than = a > b
    greater_equal = a >= b
    
    return less_than, less_equal, greater_than, greater_equal

a = 10
b = 5
lt, le, gt, ge = relational_operators(a, b)
print(f"Less than: {lt}")
print(f"Less than or equal: {le}")
print(f"Greater than: {gt}")
print(f"Greater than or equal: {ge}")

# 5. Print the smaller and larger number
def find_smaller_larger(a, b):
    smaller = a if a < b else b
    larger = a if a > b else b
    return smaller, larger

a = 10
b = 5
smaller, larger = find_smaller_larger(a, b)
print(f"Smaller number: {smaller}")
print(f"Larger number: {larger}")
