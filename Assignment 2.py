# Task 1: Check if a number is Even or Odd
print ("Assignment 2\nTask 1: Check if a number is Even or Odd")
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter an integer and try again")
print(f"{num} is an even number.") if num % 2 == 0 else print(f"{num} is an odd number.")
print ("End of Task 1")

print()
print("-"*70)
print()
# Task 2: Sum of Integers from 1 to 50 Using a Loop
print("Task 2: Sum of Integers from 1 to 50 Using a Loop")
numbers = []
for i in range(1,51):
    numbers.append(i)

total = sum(numbers)
print(f"The sum of integer from 1 to 50 is {total}")
print("End of Task 2\nThank you.")


