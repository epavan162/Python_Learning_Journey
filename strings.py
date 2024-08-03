import re

# 1. Different ways of creating a string
string1 = "Hello, World!"  # Using double quotes
string2 = 'Hello, World!'  # Using single quotes
string3 = """Hello,
World!"""  # Using triple quotes for multi-line strings

print("String1:", string1)
print("String2:", string2)
print("String3:", string3)

# 2. Concatenating two strings using + operator
string4 = "Hello, "
string5 = "Python!"
concatenated_string = string4 + string5
print("Concatenated String:", concatenated_string)

# 3. Finding the length of the string
length_of_string = len(concatenated_string)
print("Length of String:", length_of_string)

# 4. Extract a substring
substring = concatenated_string[7:13]  # Extracting 'Python'
print("Substring:", substring)

# 5. Searching in strings using index()
index_of_substring = concatenated_string.index("Python")  # Finds the index of 'Python'
print("Index of 'Python':", index_of_substring)

# 6. Matching a string against a regular expression with re.match()
pattern = re.compile(r'Hello')
match = pattern.match(concatenated_string)
print("Match found:", bool(match))

# 7. Comparing strings
string6 = "Hello, Python!"
string7 = "Hello, World!"
comparison_result = (string6 == string7)
print("Strings are equal:", comparison_result)

# 8. startsWith(), endsWith() and compareTo() (using comparison operators)
starts_with_hello = concatenated_string.startswith("Hello")
ends_with_python = concatenated_string.endswith("Python!")
print("Starts with 'Hello':", starts_with_hello)
print("Ends with 'Python!':", ends_with_python)

# 9. Trimming strings with strip()
string_with_spaces = "  Hello, Python!  "
trimmed_string = string_with_spaces.strip()
print("Trimmed String:", trimmed_string)

# 10. Replacing characters in strings with replace()
replaced_string = concatenated_string.replace("Python", "World")
print("Replaced String:", replaced_string)

# 11. Splitting strings with split()
split_string = concatenated_string.split(", ")
print("Split String:", split_string)

# 12. Converting integer objects to Strings
integer_value = 123
string_from_integer = str(integer_value)
print("String from Integer:", string_from_integer)

# 13. Converting to uppercase and lowercase
uppercase_string = concatenated_string.upper()
lowercase_string = concatenated_string.lower()
print("Uppercase String:", uppercase_string)
print("Lowercase String:", lowercase_string)
