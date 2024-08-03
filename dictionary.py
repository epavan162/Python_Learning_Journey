# Create a Dictionary with at least 5 key-value pairs of Student ID and Name
students = {
    101: "Pavan",
    102: "Giridhar",
    103: "Prasad",
    104: "Kalyan",
    105: "Prince"
}

# 1.1 Adding the values in dictionary
students[106] = "Siddharth"  # Adding a new student
print("After adding a new student:", students)

# 1.2 Updating the values in dictionary
students[102] = "Giri"  # Updating the name of student with ID 102
print("After updating a student's name:", students)

# 1.3 Accessing the value in dictionary
student_name = students.get(103, "Not Found")  # Accessing the name for student ID 103
print("The name of student with ID 103 is:", student_name)

# 1.4 Create a nested dictionary
nested_students = {
    "ClassA": {
        101: "Pavan",
        102: "Giridhar"
    },
    "ClassB": {
        103: "Prasad",
        104: "Kalyan"
    }
}

# 1.5 Access the values of nested dictionary
class_a_students = nested_students["ClassA"]  # Accessing ClassA students
print("Students in ClassA:", class_a_students)

# Accessing a specific student in ClassB
student_class_b = nested_students["ClassB"].get(104, "Not Found")
print("The name of student with ID 104 in ClassB is:", student_class_b)

# 1.6 Print the keys present in a particular dictionary
print("Keys in the students dictionary:", students.keys())

# 1.7 Delete a value from a dictionary
del students[106]  # Removing the student with ID 106
print("After deleting a student:", students)
