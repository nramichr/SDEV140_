"""
7. Random Number File Writer
Write a program that writes a series of random numbers to a file. 
Each random number should be in the range of 1 through 500. 
The application should let the user specify how many random numbers the file will hold.

8. Random Number File Reader                            
This exercise assumes you have completed Programming Exercise 7, Random Number File Writer. 
Write another program that reads the random numbers from the file, displays the numbers, then displays the following data:    
The total of the numbers 
The number of random numbers read from the file

"""


import random

MIN_NUMBER: int = 1
MAX_NUMBER: int = 500

def get_input() -> int:
    """Get the number of random numbers to generate from the user."""
    while True:
        try:
            count: int = int(input("Enter the number of random numbers to generate: "))
            if count <= 0:
                print("Please enter a positive integer.")
                continue
            return count
        except ValueError:
            print("Invalid input. Please enter a valid integer.") 

def write_random_numbers_to_file(filename: str, count: int) -> None:
    """Write a specified number of random numbers to a file."""
    with open(filename, 'w') as file:
        for _ in range(count):
            random_number: int = random.randint(MIN_NUMBER, MAX_NUMBER)
            file.write(f"{random_number}\n")

def read_random_numbers_from_file(filename: str) -> list:
    """Read random numbers from a file and return them as a list of integers."""
    numbers: list = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number: int = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid number found in file: {line.strip()}")
    return numbers

def display_numbers_stats(numbers: list) -> None:
    """Display the numbers and their statistics."""
    if not numbers:
        print("No numbers to display.")
        return

    total: int = sum(numbers)
    count: int = len(numbers)
    #I've added average calculation here to display the average of the numbers read from the file. 
    #Original excircise didn't include average. Day 6 exercise included average calculation.
    average: float = total / count

    print("Random Numbers:")
    for number in numbers:
        print(number)

    print(f"\nTotal of the Numbers: {total:,}")  # Display total with comma as thousand separator
    print(f"Number of random numbers read from the file: {count:,}")  # Display count with comma as thousand separator
    print(f"Average of the Numbers: {average:,.2f}")  # Display average with two decimal places and comma as thousand separator

def main() -> None:
    """Main function to execute the random number file writer and reader."""
    filename: str = "random_numbers.txt"
    count: int = get_input()
    write_random_numbers_to_file(filename, count)
    numbers: list = read_random_numbers_from_file(filename)
    display_numbers_stats(numbers)

if __name__ == "__main__":
    main()

print("Christian Ramirez-Flores")