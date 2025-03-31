'''
Question 1: Weather Alert System

Description: Write a program that takes a temperature input from the user and prints whether the weather is hot, cold, or moderate. If the temperature is above 30°C, print "Hot". If it's below 10°C, print "Cold". Otherwise, print "Moderate". If the temperature is exactly 25°C, print "Perfect weather!".
'''

# This program will check the temperature and give a weather update

temperature = float(input("\n\nEnter the temperature in °C: "))

# Complete the if-elif-else logic here

if temperature >= 30:
    print("Hot.")

elif temperature == 25:
    print("Perfect weather!")

elif temperature <= 10:
    print("Cold.")

else:
    print("Moderate.")
