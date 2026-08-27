"""
Day 2: Input two numbers & multiply
Instructions: 
Create a PYTHON program that prompts and receives two floating point numbers, multiplies them, and displays the result.
Be sure to provide appropriate "in code" documentation using program comments.
When complete, submit your program source code.

"""

FIRST_NUMBER=float(input("Enter the first number: "))
SECOND_NUMBER=float(input("Enter the second number: "))

OUTPUT = FIRST_NUMBER * SECOND_NUMBER

if len(str(OUTPUT)) <= len(f"{OUTPUT:,.2f}"):
    print("The product of your two numbers is:", f"{OUTPUT:,.0f}")

if len(str(OUTPUT)) >= len(f"{OUTPUT:,.2f}"):
    print("Your answer is:", f"{OUTPUT:,}")

print("Christian Ramirez-Flores :)")