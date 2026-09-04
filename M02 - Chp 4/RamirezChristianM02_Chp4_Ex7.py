"""

Write a program that calculates the amount of money a person would earn over a period of 
time if their salary is one penny the first day, two pennies the second day, and continues
to double each day. The program should ask the user for the number of days.
Display a table showing what the salary was for each day, then show the total pay at the end of the period. 
The output should be displayed in a dollar amount, not the number of pennies.

"""

input_days: str = input("Enter the number of days you would like to calculate your salary for: ")
while not input_days.isdigit() or int(input_days) <= 0:
    print("Please enter a positive integer greater than zero.")
    input_days = input("Enter the number of days you would like to calculate your salary for: ")

num_days: int = int(input_days)

pennies: int = 1
total_pennies: int = 0

print("Day\tPay")
for day in range(1, num_days + 1):
    daily_pay: float = pennies / 100
    print(f"{day}\t${daily_pay:,.2f}")
    total_pennies += pennies
    pennies *= 2

print(f"Total pay: ${total_pennies / 100:,.2f}")

print('Christian Ramirez-Flores')