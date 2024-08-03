# 1. Generate ArithmeticException without exception handling
def generate_arithmetic_exception():
    result = 10 / 0  # Division by zero
    print(result)

# Uncomment the following line to see the exception
# generate_arithmetic_exception()

# 2. Handle ArithmeticException using try-except block
def handle_arithmetic_exception():
    try:
        result = 10 / 0  # Division by zero
    except ZeroDivisionError as e:
        print("Handled ArithmeticException:", e)

handle_arithmetic_exception()

# 3. Method which throws an exception, call it without try block
def method_throws_exception():
    raise Exception("This is a thrown exception")

# Uncomment the following line to see the exception
# method_throws_exception()

# 4. Program with multiple except blocks
def multiple_catch_blocks():
    try:
        num = int("abc")  # This will raise ValueError
        result = 10 / 0   # This will raise ZeroDivisionError
    except ValueError as ve:
        print("Caught ValueError:", ve)
    except ZeroDivisionError as zde:
        print("Caught ZeroDivisionError:", zde)

multiple_catch_blocks()

# 5. Throw exception with your own message
def throw_custom_exception():
    raise Exception("This is a custom exception message")

# Uncomment the following line to see the exception
#throw_custom_exception()

# 6. Create your own exception
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def raise_custom_exception():
    raise MyCustomException("This is my custom exception")

# Uncomment the following line to see the exception
#raise_custom_exception()

# 7. Program with finally block
def finally_block_example():
    try:
        result = 10 / 2
        print("Result:", result)
    except ZeroDivisionError:
        print("Caught division by zero")
    finally:
        print("This will always execute")

finally_block_example()

# 8. Generate ArithmeticException
def generate_arithmetic_exception_again():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Generated ArithmeticException:", e)

generate_arithmetic_exception_again()

# 9. Generate FileNotFoundException
def generate_file_not_found_exception():
    try:
        with open("nonexistent_file.txt", 'r') as file:
            contents = file.read()
    except FileNotFoundError as e:
        print("Caught FileNotFoundException:", e)

generate_file_not_found_exception()

# 10. Generate ClassNotFoundException
def generate_class_not_found_exception():
    try:
        __import__('non_existent_module')  # Trying to import a non-existent module
    except ModuleNotFoundError as e:
        print("Caught ClassNotFoundException:", e)

generate_class_not_found_exception()

# 11. Generate IOException
def generate_io_exception():
    try:
        with open("/root/forbidden_file.txt", 'r') as file:
            contents = file.read()
    except IOError as e:
        print("Caught IOException:", e)

generate_io_exception()

# 12. Generate NoSuchFieldException
def generate_no_such_field_exception():
    class Example:
        pass

    try:
        example_instance = Example()
        print(example_instance.non_existent_field)
    except AttributeError as e:
        print("Caught NoSuchFieldException:", e)

generate_no_such_field_exception()
