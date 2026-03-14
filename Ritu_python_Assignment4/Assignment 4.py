# Assignment 4: Files, Exceptions, and Errors in Python
# Task 1:  Read a File and Handle Errors

print("Assignment 4: Files, Exceptions, and Errors in Python")
print("Task 1:  Read a File and Handle Errors ")
print()

# Opens and reads a text file named sample.txt.
try:
    with open("sample.txt", 'rt') as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("File 'sample.txt' is empty")

# Prints its content line by line.

        else:
            print("File 'sample.txt' is successfully opened.")
            print("\nReading the file content:")
            for line_num, line in enumerate (lines,1):
                print(f"line {line_num}: {line.rstrip()}")

# Handles errors gracefully if the file does not exist.

except FileNotFoundError as file_error:
    print("Error. File 'sample.txt' not found!")
    print(file_error)

print()
print ("End of Task 1")

print()
print("-"*70)
print()

#Task 2:  Write and Append Data to a File

print("Task 2:  Write and Append Data to a File")
print()

def add_punctuation_if_missing (text, punctuation='.'):
    """
    Checks for common punctuation
    Also adds punctuation if it is not end with it.
    """
    if not text:
        return text
    common_punctuation = [",",".","!","?"]
    for p in common_punctuation:
        if text.endswith(p):
         return text
    return text + punctuation


# Takes user input and writes it to a file named output.txt.

user_input = input("Enter text to write to the file: ")
user_input = add_punctuation_if_missing(user_input)

with open("output.txt", 'wt') as fh:
    fh.write(user_input)
    print(f"'{user_input}' is successfully written to output.txt")

print()

# Appends additional data to the same file.

additional_input = input("Enter additional text to append to the file: ")
additional_input = add_punctuation_if_missing(additional_input)

with open("output.txt", 'at') as fh:
    fh.write("\n" + additional_input)
    print(f"'{additional_input}' is successfully appended to output.txt")

# Reads and displays the final content of the file.

print("Final content of output.txt:")
print()

with open("output.txt", 'rt') as fh:
    content = fh.read()
    print(content)

print()
print("End of Task 2\nThank you.")

