# Day 3 Calculate Grade Nested if
# Note: User will input a score and the program will
#   output a grade (A - F) on a 10 point scale
# Joseph Hollenbach  1/27/2021
#   J. Treacy - added code to validate correct 0-100 range input
#                as well as numeric digits input

"""
Take the above program that calculates grades from input scores and revise it to add a while loop to allow multiple scores to input in a single run using a user prompt for another run.
Reference page 172 Program 4-1 that uses a keep_going variable for end of loop test.
"""

# Define module
def main():

    # Get test score from user
    scoreSt = input('Please enter your score (0-100): ')
    # check if valid digits Convert score to integer number
    if not (scoreSt.isdigit()):
        grade = "Invalid Numeric Integer Score input"
    else: 
        score = int(scoreSt)  # valid so convert and continue
        # Determine letter grade
        if score > 100:
            grade = "Invalid score too high "
        elif score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        elif score >= 0:
            grade = 'F'
        else:
            grade = "Invalid score too low "
        print("Your entered grade is:", grade) # Output letter grade based on score
    while True:
        # Ask user if they want to continue
        ask = input("Do you want to enter another score? (y/n): ")
        if ask.lower() == 'y':
            main()  # This calls for the main function again
            break
        elif ask.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")    
main()

print('Christian Ramirez-Flores')