"""
Day 05 - Simulating Pair of Dice
Make use of the random number feature in Python to simulate the rolling of a pair of dice.
Get input from operator for the number of rolls and retrieve an optional seed number (zero to use the system clock).
Encase this in a while loop to allow multiple runs.
Experiment with two runs with no seed number, two runs with the same seed number and a run with a different seed number. 
"""

import random


    #Simulates rolling a pair of dice for a given number of times.
def roll_dice(num_rolls):
    for i in range(1, num_rolls +1):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f" Roll {i:02d}: [{die1}] [{die2}] Total: {total}")
    #While loop to allow multiple runs of the program.
while True:
    print("><" * 13)
    print(" Dice Rolling Simulation ")
    print("><" * 13)
    #Gets the number of rolls from the operator and handles invalid input.
    try:
        rolls_input: str = input("Enter the number of rolls (or 'exit' to quit): ")
        if rolls_input.lower() == 'exit':
            print("Exiting the Simulation. Goodbye!")
            break

        num_rolls: int = int(rolls_input)
        if num_rolls <= 0:
            print("Please enter a positive integer for the number of rolls.")
            continue
    except ValueError:
        print("Invalid input. Please enter a positive integer for the number of rolls.")
        continue
    #Retrieves optional seed number from the operator and handles invalid input.
    try:
        seed_input: str = input("Enter a seed number (or 0 to use the system clock): ")
        seed_number: int = int(seed_input)
    except ValueError:
        print("Invalid input. Defaulting to 0 (system clock).")
        seed_number = 0 
    #Apply seed config based on user input.
    if seed_number == 0:
        print("Initializing with System Clock (default seed).")
        random.seed(None)  # Use system clock for seed
    else:
        print(f"Initializing with Seed Number: {seed_number}")
        random.seed(seed_number)  # Use user-provided seed
    roll_dice(num_rolls)

print("Christian Ramirez-Flores")