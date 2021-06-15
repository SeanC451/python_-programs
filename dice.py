# DnD Dice
# Susan L. Carr
# Program inputs from user the number of dice, number of sides and 
# number to add on to the total rolled. Ex: 1d4+2 or 3d6+0.
# Result is printed with variables and total rolled.

import os
import random

def roll_dice(x, y, z):
    count = 1                                                  # Set counter at 1 for first iteration.

    rolled_num = 0                                             # Initialize number rolled counters.
    roll_total = 0

    dice = int(x)                                              # Convert strings to integers for math operations.
    sides = int(y)
    addon = int(z)

    while(count <= dice):                                      # Loop to iterate for each number of dice user wishes to roll.
        rolled_num = random.randint(1, sides)                  # Generate random number from 1 to sides of dice.
        # print(f"Die #{count} is {rolled_num}")               # Make sure of randomness. Uncomment to debug.
        roll_total += rolled_num                               # Accumulate value
        count += 1                                             # Increment counter.

    return roll_total + addon

os.system('cls')

numDice = input("Enter number of dice: ")                       # Input user defined variables.
numSides = input("Enter number of sides: ")
numAddon = input("Enter add-on: ")

roll = roll_dice(numDice, numSides, numAddon)                   # Pass variables to roll_dice function.

print(f"Your roll of {numDice}d{numSides}+{numAddon} is {roll}.")
