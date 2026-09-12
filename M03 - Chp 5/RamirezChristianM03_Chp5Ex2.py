"""

2. Sales Tax Program Refactoring
Programming Exercise #6 in Chapter 2 was the Sales Tax program. 
For that exercise, you were asked to write a program that calculates and displays the county 
and state sales tax on a purchase. If you have already written that program, redesign it so the subtasks 
are in functions. If you have not already written that program, write it using functions.

Previous:
Write a prgoram that will ask the user to enter the amount of a purchase. The program
should then compute the state and county sales tax. Assume the state sales tax is 5 percent and the county sales tax 2.5 percent.
The program should display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax,
and the total of the sale (which is the sum of the amount of purchase plus the total sales tax).

*** All that needs to be done is define functions to each section. Original code lacks validation methods/proper code execution.

"""

#Constants for the tax rates
STATE_TAX = 0.05
COUNTY_SALES_TAX = 0.025

def main():
    purchase_amount = get_purchase_amount()
    state_tax_amount = calculate_state_tax(purchase_amount)
    county_sales_tax_amount = calculate_county_tax(purchase_amount)
    total_sales_tax = state_tax_amount + county_sales_tax_amount
    total_purchase_amount = purchase_amount + total_sales_tax
    display_results(purchase_amount, state_tax_amount, county_sales_tax_amount, total_sales_tax, total_purchase_amount)

def get_purchase_amount():
    print("What's the amount of the purchase you've made?")
    return float(input())

def calculate_state_tax(purchase_amount):
    return purchase_amount * STATE_TAX

def calculate_county_tax(purchase_amount):
    return purchase_amount * COUNTY_SALES_TAX

def display_results(purchase_amount, state_tax_amount, county_sales_tax_amount, total_sales_tax, total_purchase_amount):
    print("Sale Summary:")
    print("Total state tax amount:", f"${state_tax_amount:.2f}")
    print("Total county sales tax amount:", f"${county_sales_tax_amount:.2f}")
    print("Total sales tax:", f"${total_sales_tax:.2f}")
    print("Total purchase amount:", f"${total_purchase_amount:.2f}")
    
if __name__ == "__main__":
        main()

print("Christian Ramirez-Flores")