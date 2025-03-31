'''
Question 2: Grading System
Description: Write a program that takes a student's score as input and assigns a grade based on the following criteria:

90 or above: "A"
80-89: "B"
70-79: "C"
60-69: "D"
Below 60: "F"
'''

# This program will assign grades based on the score

score = float(input("Enter the student's score: "))

# Complete the if-elif-else logic to assign grades

if score >= 90 and score <= 100:
    print("\nThe student has an: A.")
elif score >= 80 and score <= 89:
    print("\nThe student has an: B.")
elif score >= 70 and score <= 79:
    print("\nThe student has an: C.")
elif score >= 60 and score <= 69:
    print("\nThe student has an: D.")
elif score < 60 and score >= 0:
    print("\nThe student has an: F.")
else:
    print("The score is either too low or too high!")