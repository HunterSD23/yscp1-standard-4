"""
Question 3: Nested Age Check
Description: Write a program that checks a person's age and prints a message. The program should have the following logic:

If the person is below 13, print "Child".
If the person is between 13 and 19, print "Teenager".
If the person is between 20 and 64, print "Adult".
If the person is 65 or older, print "Senior".
If the person's age is 18 or 21, print "Young Adult".
"""

# This program will check age categories

age = int(input("\nEnter your age: "))

# Add if-elif-else logic here with nested conditions

if age >= 65:
    print("You are a Senior.\n")
elif age >= 20 and age <=64:
    if age == 21:
        print("You are a Young Adult.")
    else:
        print("You are an Adult.")
elif age >= 13 and age <= 19:
    if age == 18:
        print("You are a Young Adult.")
    else:
        print("You are a Teenager.")
elif age < 13 and age >=0:
    print("You are a Child.")
else:
    print("The age you have entered is either too old or too young.")