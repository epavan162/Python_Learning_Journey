import os

# 1. Write a program to read a text file
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(f"Contents of {filename}:")
            print(contents)
    except IOError:
        print(f"Error: could not read file {filename}")

# 2. Write a program to write text to a .txt file using InputStream
def write_file(filename, text):
    try:
        with open(filename, 'w') as f:
            f.write(text)
        print(f"Text written to {filename} successfully.")
    except IOError:
        print(f"Error: could not write to file {filename}")

# 3. Write a program to read a file stream
def read_file_stream(filename):
    try:
        with open(filename, 'rb') as f:
            contents = f.read()
            print(f"Binary contents of {filename}:")
            print(contents)
    except IOError:
        print(f"Error: could not read file {filename}")

# 4. Write a program to read a file stream with random access
def read_file_random_access(filename):
    try:
        with open(filename, 'rb') as f:
            f.seek(0)  # Move to the start of the file
            print("Reading from the beginning:")
            print(f.read())
            f.seek(5)  # Move to the 5th byte
            print("Reading from the 5th byte:")
            print(f.read())
    except IOError:
        print(f"Error: could not read file {filename}")

# 5. Write a program to read a file and adjust to a particular index using seek()
def read_file_with_seek(filename):
    try:
        with open(filename, 'r') as f:
            f.seek(10)  # Move to the 10th character
            print("Contents from the 10th character:")
            print(f.read())
    except IOError:
        print(f"Error: could not read file {filename}")

# 6. Write a program to check whether a file has read and write access permissions
def check_file_permissions(filename):
    read_permission = os.access(filename, os.R_OK)
    write_permission = os.access(filename, os.W_OK)
    print(f"Read permission for {filename}: {'Yes' if read_permission else 'No'}")
    print(f"Write permission for {filename}: {'Yes' if write_permission else 'No'}")

if __name__ == '__main__':
    filename = "example.txt"
    text_to_write = "Hello, world! This is a test file."

    # Test each function
    write_file(filename, text_to_write)           # Write text to the file
    read_file(filename)                           # Read the file
    read_file_stream(filename)                    # Read file as binary stream
    read_file_random_access(filename)             # Read file with random access
    read_file_with_seek(filename)                 # Read file from a specific index
    check_file_permissions(filename)              # Check file permissions
