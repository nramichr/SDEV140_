"""
Day 09 - 
Modify Day 07 Roll of Dice program to make use of Die() class found in program CH_10_Die_ClassDefined.py 

Download both program. The modify the Day 7 program to use the Die() class in the Ch_10_

I'm just modifying my original file from Day 07

"""

import random

#Imports class from "Ch_10_Die_ClassDefined" ---- given that the file exists in the same folder as current python file. 
from Ch_10_Die_ClassDefined import Die


def roll_dice(num_rolls):
    
    #Initialize a list to hold the tally counts for sums 2 through 12
    tally = [0] * 13  # Index 0 and 1 will be unused, index 2-12 will hold counts

    #Creates two Die objects using the imported class
    die1 = Die()
    die2 = Die()

    #Rolls each die with random function
    for i in range(num_rolls):
        die1.roll()
        die2.roll()
        total = die1.get_roll() + die2.get_roll()
        tally[total] += 1

    return tally
    #Rest of my original code
while True:
    print(" ")
    print("=" * 14)
    print("Dice Simulator")
    print("=" * 14)
    print(" ")
    #Gets the number of rolls from the operator and handles invalid input.
    try:
        rolls_input: int = input("Enter the number of rolls or 'exit' to quit: ")
        if rolls_input.lower() == 'exit':
            break

        num_rolls: int = int(rolls_input)
        if num_rolls <= 0:
            print("Please enter a positive integer for the number of rolls.")
            continue
    except ValueError:
        print("Invalid input. Please enter a positive integer for the number of rolls.")
        continue

    #Roll the dice and get the tally
    tally = roll_dice(num_rolls)

    #Display the results from rolled dice.
    print("\nResults:")
    print(f"{'Sum':<5}{'Tally/Count':<10}{'Percentage':<15}{'Expected Percentage':<15}")
    expected_percentages = [0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    
    for sum_value in range(2, 13):
        percentage = (tally[sum_value] / num_rolls) * 100
        expected_percentage = expected_percentages[sum_value] * 100
        print(f"{sum_value:<5}{tally[sum_value]:<10}{percentage:<15.2f}{expected_percentage:<15.2f}")


print("Christian Ramirez-Flores")
