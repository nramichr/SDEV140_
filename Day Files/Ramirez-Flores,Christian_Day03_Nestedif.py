"""
Write a program that inputs a score from zero to 100.  Use If statements to calculate grade on a ten point scale.

90-100 A
80-89 B
70-79 C
60-69 D
<60 F
"""
# Defines module
def main():

    print('Enter a score from 0 to 100 to calculate the grade on a ten point scale.')

    score:float = float(input('Please enter your score (0-100): '))

    if score > 100:
        print('That grade is not possible.')
    elif score >= 90:
        print('Your grade is: A')
    elif score >= 80:
        print('Your grade is: B')
    elif score >= 70:
        print('Your grade is: C')
    elif score >= 60:
        print('Your grade is: D')
    elif score >= 0:
        print('Your grade is: F')
    else:
        print('That grade is not possible, your score is too low.')
main()

print('Christian Ramirez-Flores')