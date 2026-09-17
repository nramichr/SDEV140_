"""

Ex. 1
Write a program that asks the user to enter a distance in kilometers, then uses a function to convert that distance to miles.
The conversion formula is as follows:

Miles = Kilometers x 0.6214

"""


#Global constant
CONVERSION = 0.6214

def main():
    try: 
        #Calls for user input 
        km_input: float = float (input("Enter a distance in kilometers: "))
        convert_to_miles(km_input)

    except ValueError:
        print("Error: Please enter a valid numerical value.")

def convert_to_miles(kilometers):
    miles: float = kilometers * CONVERSION
    print(f"{kilometers:,.2f} kilometers is equal to  {miles:,.2f} miles.")

if __name__ == "__main__":
    main()