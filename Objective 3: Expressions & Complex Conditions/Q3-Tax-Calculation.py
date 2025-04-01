'''
Question 3: Tax Calculation
Description: Write a program that calculates the tax on a purchase based on the price. The tax rate should be 8% if the price is under $100 and 10% if it’s $100 or more.
'''

# This program calculates the tax based on price

price = float(input("Enter the price of the item: $"))

# Use complex conditions to calculate the tax rate
if price < 100:
    TAX_RATE = 0.08
    price = price + (price * TAX_RATE)
    print(f"The total price of your item with 8% tax is: ${price:.2f}")
elif price >= 100: 
    TAX_RATE = 0.10
    price = price + (price * TAX_RATE)
    print(f"The total price of your item with 10% tax is: ${price:.2f}")