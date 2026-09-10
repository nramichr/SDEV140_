"""
Day 07 - Simulating Pair of Dice with Tally and Percentages


Write a program that takes the number of times to roll two dice from the console.  
Do a tally of the result number (2 through 12) in an indexed list.  
When program completes this experiment, you will display the tallies from the list and use them to calculate the percent of times each number occurred. 

Additional item: Store the expected percent for each result number in a stable table and display these alongside the corresponding results of your experiments in your display.  
If you run two different experiments, one using a relatively small number (<500) and another with a large number (say a million), you will see a demonstration of the law of large numbers:  
The larger your sample size, the closer to the theoretical probability you will get.

Hint: Use formatted print lines to make results professionally lined up.  Reference section 2.10 (p70-78) for more details. 

"""
import random


def roll_dice(num_rolls):
    
    # Initialize a list to hold the tally counts for sums 2 through 12
    tally = [0] * 13  # Index 0 and 1 will be unused, index 2-12 will hold counts

    for i in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        tally[total] += 1

    return tally
while True:
    print(" ")
    print("=" * 14)
    print("Dice Simulator")
    print("=" * 14)
    print(" ")
    # Gets the number of rolls from the operator and handles invalid input.
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

    # Roll the dice and get the tally
    tally = roll_dice(num_rolls)

    # Display the results from rolled dice.
    print("\nResults:")
    print(f"{'Sum':<5}{'Tally/Count':<10}{'Percentage':<15}{'Expected Percentage':<15}")
    expected_percentages = [0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    
    for sum_value in range(2, 13):
        percentage = (tally[sum_value] / num_rolls) * 100
        expected_percentage = expected_percentages[sum_value] * 100
        print(f"{sum_value:<5}{tally[sum_value]:<10}{percentage:<15.2f}{expected_percentage:<15.2f}")


print("Christian Ramirez-Flores")
