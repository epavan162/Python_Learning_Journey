# if you define multiple methods with the same name, the last one defined will override the previous ones.
# only use the latest defined method. 

# First product method.
# Takes two argument and print their
# product


def product(a, b, c):
	p = a * b
	print(p)

# Second product method
# Takes three argument and print their
# product


def product(a, b, c):
	p = a * b*c
	print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 5)
