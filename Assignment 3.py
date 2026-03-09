# Assignment 3 : Functions & Modules in Python
# Task 1: Calculate Factorial Using a Function

print("Assignment 3 \nTask 1: Calculate Factorial Using a Function")

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter an integer.")

print(f"factorial of {num} is {factorial(num)}")

print ("End of Task 1")

print()
print("-"*70)
print()

# Task 2: Task 2: Using the Math Module for Calculations
print("Task 2: Using the Math Module for Calculations")

import math

while True:
    try:
        n = float(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid number.")
#Calculate square root
if n >= 0:
    Square_root = math.sqrt(n)
    print(f"The square root of {n} is {Square_root}")
else:
    print("Error. Cannot calculate square root of a negative number.")

#Calculate natural logarithm
if n >  0:
    Logarithm = math.log(n)
    print(f"The logarithm of {n} is {Logarithm}")
elif n == 0:
    print("Log of zero is undefined. Please enter a positive number.")
else:
    print("Error. Cannot calculate natural logarithm of a negative number.")

#Calculate sine of a number
Sine = math.sin(n)
print(f"The sine of {n} in radians is {Sine}")
print("End of Task 2\nThank you.")