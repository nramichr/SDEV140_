"""

8. Name Search
If you have downloaded the source code you will find a file in the Chapter 07 folder named popular_names.txt. 
This file contains a list of the 400 most popular names given to children born in the United States from the year 2000 through 2009.
Write a program that reads the contents of file into a list. The user should be able to enter a name and the program 
will display a message indicating whether the name was among the most popular.

(You can access the Computer Science Portal at www.pearsonhighered.com/gaddis.)

"""

def main():
    with open ('BoyNames.txt', 'r') as file:
        boy_names = [line.strip() for line in file]
    with open ('GirlNames.txt', 'r') as file:
        girl_names = [line.strip() for line in file]

    name = input('Enter a name:')

    if name in boy_names and name in girl_names:
        print(f'{name} was one of the 400 most popular names, for both boys and girls.')
    elif name in boy_names
        print(f'{name} was one of the 400 most popular boy names.')
    elif name in girl_names
        print(f'{name} was on of the 400 most popular girl names.')
    else:
        print(f"{name} wasn't among the most popular names.")