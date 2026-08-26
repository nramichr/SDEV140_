"""
    6.
    Write a program that will ask the user to enter the amount of a purchase. 
    The program should then compute the state and county sales tax. Assume the 
    state sales tax is 5 percent and the county sales tax is 2.5 percent. The 
    program should display the amount of the purchase, the state sales tax, 
    the county sales tax, the total sales tax, and the total of the sale (which is the sum of the amount of purchase plus the total sales tax).

    Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.
"""


print("What's the amount of the purchase you've made?")
purchase_amount = float(input())

STATE_TAX = 0.05
COUNTY_SALES_TAX = 0.025

state_tax_amount = purchase_amount * STATE_TAX
county_sales_tax_amount = purchase_amount * COUNTY_SALES_TAX
total_sales_tax = state_tax_amount + county_sales_tax_amount
total_purchase_amount = purchase_amount + total_sales_tax

print("Sale Summary:")
print("Total state tax amount:", f"${state_tax_amount:.2f}")
print("Total county sales tax amount:", f"${county_sales_tax_amount:.2f}")
print("Total sales tax:", f"${total_sales_tax:.2f}")
print("Total purchase amount:", f"${total_purchase_amount:.2f}")