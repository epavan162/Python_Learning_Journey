# 1. Function to add integer values of an array
def add_array_elements(arr):
    return sum(arr)

# 2. Function to calculate the average value of an array of integers
def average_array(arr):
    return sum(arr) / len(arr) if arr else 0

# 3. Program to find the index of an array element
def find_index(arr, value):
    return arr.index(value) if value in arr else -1

# 4. Function to test if an array contains a specific value
def contains_value(arr, value):
    return value in arr

# 5. Function to remove a specific element from an array
def remove_element(arr, value):
    return [item for item in arr if item != value]

# 6. Function to copy an array to another array
def copy_array(arr):
    return arr.copy()

# 7. Function to insert an element at a specific position in the array
def insert_element(arr, index, value):
    arr.insert(index, value)
    return arr

# 8. Function to find the minimum and maximum value of an array
def min_max_array(arr):
    return min(arr), max(arr)

# 9. Function to reverse an array of integer values
def reverse_array(arr):
    return arr[::-1]

# 10. Function to find the duplicate values of an array
def find_duplicates(arr):
    seen = set(arr)
    duplicates = [x for x in seen if arr.count(x)>1]
    return duplicates

# 11. Program to find the common values between two arrays
def common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))

# 12. Method to remove duplicate elements from an array
def remove_duplicates(arr):
    return list(set(arr))

# 13. Method to find the second largest number in an array
def second_largest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[-2] if len(unique_arr) > 1 else None

# 14. (Duplicate of 13)

# 15. Method to find number of even and odd numbers in an array
def count_even_odd(arr):
    even_count = sum(1 for x in arr if x % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

# 16. Function to get the difference of largest and smallest value
def range_difference(arr):
    return max(arr) - min(arr) if arr else 0

# 17. Method to verify if the array contains two specified elements (12, 23)
def contains_two_elements(arr, elem1, elem2):
    return elem1 in arr and elem2 in arr

# 18. Program to remove duplicate elements and return the new array
def remove_duplicates_and_return(arr):
    return list(set(arr))

# Example Usage
arr = [1, 2, 3, 4, 5, 5, 6]
print("Sum:", add_array_elements(arr))
print("Average:", average_array(arr))
print("Index of 4:", find_index(arr, 4))
print("Contains 3:", contains_value(arr, 3))
print("Remove 5:", remove_element(arr, 5))
print("Copy:", copy_array(arr))
print("Insert 10 at index 2:", insert_element(arr.copy(), 2, 10))
print("Min and Max:", min_max_array(arr))
print("Reversed:", reverse_array(arr))
print("Duplicates:", find_duplicates(arr))
print("Common values with [4,5,6]:", common_values(arr, [4,5,6]))
print("Remove duplicates:", remove_duplicates(arr))
print("Second largest:", second_largest(arr))
print("Even and Odd count:", count_even_odd(arr))
print("Range difference:", range_difference(arr))
print("Contains 12 and 23:", contains_two_elements(arr, 12, 23))
print("Remove duplicates and return:", remove_duplicates_and_return(arr))
