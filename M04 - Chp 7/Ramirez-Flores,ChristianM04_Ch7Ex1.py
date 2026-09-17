"""

1.
Design a program that asks the user to enter a store's sales for each day of the week.
The amounts should be stored in a list. 
Use a loop to calculate the total sales for the week and display the result

"""

def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #Pre-creates a "dummy" list with 7 slots because there are 7 " " in days
    sales = [0.0] * len(days)

    #User input and stores in list which now will hold actual values
    for i in range (len(days)):
        sales[i] = float(input(f"Enter the sale for {days[i]}: $"))

    #Calculates total sales
    total = 0
    for amount in sales:
        total += amount
    
    print(f"\nTotal sales for the week: ${total:,.2f}")
main()

print("Christian Ramirez-Flores")