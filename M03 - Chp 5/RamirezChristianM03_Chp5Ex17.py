"""

17. Prime Number List
This exercise assumes that you have already written the function in Programming Exercise 16. 
Write another program that displays all of the prime numbers from 1 to 100. 
The program should have a loop that calls the  function.

"""
#returns True if prime number and if not considered False.
def is_prime(number):
    if number <= 1:
        return False

    for test in range(2,number):
        if number % test == 0:
            return False

    return True

def main():
    print("Prime numbers from 1 through 100:")
    #loops throughout all #'s 1-100 
    for value in range(1,101):
        if is_prime(value):
            print(value)
if __name__ == "__main__":
    main()


print("Christian Ramirez-Flores")