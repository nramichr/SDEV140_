"""
6. Average of Numbers                           
Assume a file containing a series of integers is named numbers.txt and exists on the computer(s) disk.
Write a program that calculates the average of all the numbers stored in the file.

9. Exception Handing                           
Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
It should handle any exceptions that are raised when the file is opened and data is read from it.                            
It should handle any exceptions that are raised when the items that are read from the file are converted to a number.

Used numbers.txt file from canvas module with numbers: 22,14,-99



"""

def main() -> None:
    # Specify the filename through path to file destination.
    filename: str = r"C:\Users\jrami\OneDrive\Desktop\Classes\SDEV140\numbers.txt"
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        #Stores the total and count of numbers to calculate the average.
        total: int = 0
        count: int = 0
        for line in lines:
            total += int(line)
            count += 1
        #Calculates the average and prints result out in a formatted form.
        average = total/count
        print (f"Average: {average}")

    except FileNotFoundError:
        print("Error: The file 'numbers.txt' was not found.")
    except OSError: # Handles disk/permission errors when opening the file.
        print("Error: Could not read the file 'numbers.txt'.")
    except ValueError:
        print("Error: One or more lines in the file could not be converted to an integer.")
    except ZeroDivisionError:
        print("Error: The file is empty, cannot divide by zero.")
#Validates if the script is being run directly and calls the main function.
if __name__ == "__main__":
    main()

print("Christian Ramirez-Flores")