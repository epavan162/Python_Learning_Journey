# 1. Print “Bright IT Career” ten times using a for loop
for _ in range(10):
    print("Bright IT Career")

# 2. (Java program) Print 1 to 20 numbers using the while loop.
for i in range(1,21):
    print(i)

# 3. Equal operator and not equal operators
def equal_not_equal(a, b):
    return a == b, a != b

num1 = 10
num2 = 5
equal, not_equal = equal_not_equal(num1, num2)
print(f"Equal: {equal}")
print(f"Not Equal: {not_equal}")

# 4. Print odd and even numbers
def odd_even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            print(f"Even: {i}")
        else:
            print(f"Odd: {i}")

odd_even_numbers(10)

# 5. Print largest number among three numbers
def largest_of_three(a, b, c):
    return max(a, b, c)

num1 = 10
num2 = 20
num3 = 15
largest = largest_of_three(num1, num2, num3)
print(f"Largest number: {largest}")

# 6. Print even numbers between 10 and 20 using while
i = 10
while i <= 20:
    if i % 2 == 0:
        print(f"Even: {i}")
    i += 1

# 7. Print 1 to 10 using the do-while loop statement
# Python does not have a do-while loop, so we use a while loop with an initial condition.
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

# 8. Find Armstrong number or not
def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    sum_of_powers = sum(int(digit) ** power for digit in num_str)
    return sum_of_powers == number

number = 153
print(f"Armstrong number: {is_armstrong(number)}")

# 9. Find if a number is prime or not
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number//2) + 1):
        if number % i == 0:
            return False
    return True

number = 29
print(f"Prime number: {is_prime(number)}")

# 10. Find if a number is palindrome or not
def is_palindrome(number):
    return str(number) == str(number)[::-1]

number = 121
print(f"Palindrome: {is_palindrome(number)}")

# 11. Check whether a number is EVEN or ODD using switch
def even_odd_switch(number):
    switch = {
        0: "Even",
        1: "Odd"
    }
    return switch[number % 2]

number = 10
print(f"Even or Odd: {even_odd_switch(number)}")

# 12. Print gender (Male/Female) according to given M/F using switch
def gender_switch(gender):
    switch = {
        'M': "Male",
        'F': "Female"
    }
    return switch.get(gender, "Unknown")

gender = 'M'
print(f"Gender: {gender_switch(gender)}")
