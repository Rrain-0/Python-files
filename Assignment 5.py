# Assignment 5: Data Structures and Strings in Python
#Task 1: Create a Dictionary of Student Marks

print("Assignment 5\nTask 1: Create a Dictionary of Student Marks")

# Creates a dictionary where student names are keys and their marks are values
students_marks = {
    "John Williams": 89,
    "Alice": 67,
    "Carol": 85,
    "Bob": 90,
    "Max": 92,
    "Ella": 79,
    "Ross": 95,
    "Charles": 73,
    "John Basil": 70
}

print(f"Students attending the class are:")
for student in students_marks.keys():
    print(f"   {student}")

while True:
    #Asks the user to input a student's name.
    student_name = input("Enter a student name to check their marks or type 'quit' to exit: ")

    if student_name.lower() == "quit":
        print("Thank you for using this program.")
        break

    if not student_name.strip():
        print("Please enter a valid name.")
        continue

    # Retrieves and displays the corresponding marks (includes case insensitivity)
    found = False
    exact_match = []

    for name, marks in students_marks.items():
        if name.lower() == student_name.lower():
            print(f"The marks of {student_name} is {marks}")
            found = True
            break

        elif student_name.lower() in name.lower() or name.lower() in student_name.lower():
            exact_match.append((name, marks))

    # If the student’s name is not found, display an appropriate message
    if not found:
        print(f"Student '{student_name}' is not found in the database")

    # Suggestions for names in case of wrong entries
        suggestions = []
        for name in students_marks.keys():
            if name[0].lower() == student_name[0].lower():
             suggestions.append(name)
        if suggestions:
            print("Did you mean: ")
            for suggestion in suggestions:
                print(f"   {suggestion}")

            #response = input("Is this the student you are looking for? (yes/no): ")
            choice = input("Enter the correct name from the list above or type 'no' to cancel: ")
            if choice in students_marks:
                print(f"The marks of {choice} is {students_marks[choice]}")

            elif choice.lower() == "no":
                print("Terminating the suggestion operation.")

            else:
                print("Please try again with a different name.")

        else:
               print(f"No similar name is found in the database")
               print("Here are all the students in the database: ")
               for student in students_marks.keys():
                   print(f"   {student}")

print ("End of Task 1")

"""
There are some flaws in Task 1 I don't know how to solve. 
1.The suggestion part; It is not smooth flowing in cases like students 
with same name. Even the smallest difference ie. different cases leads 
to 'name not found'
2. Even though I have considered case insensitivity from user input, it 
doesn't act in the suggestion part. The issue remains.
"""

print()
print("-"*70)
print()

# Task 2: Demonstrate list slicing
print("Task 2: Demonstrate list slicing")

#  Creates a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("Original list: ", numbers)

#  Extracts the first five elements from the list.
first_five_elements = numbers[:5]
print("First five elements: ", first_five_elements)

#  Reverses these extracted elements.
reversed_elements = first_five_elements[::-1]
print("Reversed first five elements: ", reversed_elements)

print()
print("End of Task 2\nThank you.")
print("-"*70)


