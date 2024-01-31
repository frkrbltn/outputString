# lab1KarabulutF.py
# Furkan Karabulut (fkarabu)
# Class: CSC 205-002
# Date: 1/17/2024

# This program will accept an input variable from user for the number as amount of money
# The program will return the amount of coins for the change in dollors, half dollors 
# quarters, dimes, nickels, and pennies. then it will return a total count of coins.

# Constant values for the coins
DOLLAR_VALUE = 1.00
HALF_DOLLAR_VALUE = 0.50
QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
PENNY_VALUE = 0.01

# Input: amount of money
money = float(input("Enter the total amount of money: $"))

# 1. Convert the amount of money to dollors as integer
dollors = int(money // DOLLAR_VALUE)
# 2. Convert the amount of money to half dollors
half_dollors = int((money - dollors) // HALF_DOLLAR_VALUE)
# 3. Convert the amount of money to quarters
quarters = int((money - dollors - half_dollors * HALF_DOLLAR_VALUE) // QUARTER_VALUE)
# 4. Convert the amount of money to dimes
dimes = int((money - dollors - half_dollors * HALF_DOLLAR_VALUE - quarters * QUARTER_VALUE) // DIME_VALUE)
# 5. Convert the amount of money to nickels
nickels = int((money - dollors - half_dollors * HALF_DOLLAR_VALUE - quarters * QUARTER_VALUE - dimes * DIME_VALUE) // NICKEL_VALUE)
# 6. Convert the amount of money to pennies
pennies = int((money - dollors - half_dollors * HALF_DOLLAR_VALUE - quarters * QUARTER_VALUE - dimes * DIME_VALUE - nickels * NICKEL_VALUE) // PENNY_VALUE)
# 7. Convert the amount of money to total coins
total_coins = dollors + half_dollors + quarters + dimes + nickels + pennies
print('')
print("Fewest coins for $" + str(money))
print('==========================')
print('Coin Type           Number')
print('--------------------------')
print(f'{"Dollars":<18}{dollors:>8}')
print(f'{"Half-Dollars":<18}{half_dollors:>8}')
print(f'{"Quarters":<18}{quarters:>8}')
print(f'{"Dimes":<18}{dimes:>8}')
print(f'{"Nickels":<18}{nickels:>8}')
print(f'{"Pennies":<18}{pennies:>8}')
print('--------------------------')
print(f'{"Total coins":<18}{total_coins:>8}')
