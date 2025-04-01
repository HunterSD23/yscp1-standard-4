'''
Question 3: Nested Loops (Multiplication Table)
Description: Write a program that uses nested loops to print the multiplication table for numbers 1 to 5.
'''

# This program will print the multiplication tables from 1 to 5 
number = [1, 2, 3, 4, 5]

# Use a for loop to iterate through the numbers for each table
for i in range(1):
    for x in range(1, 6):
        number = [(1*x), (2*x), (3*x), (4*x), (5*x)]
        print(number)
    # Use a nested loop to print the table for each number
    