print("What's the amount of the purchase you've made?")
purchase_amount = float(input())
state_tax = 0.05
county_sales_tax = 0.025
state_tax_amount = purchase_amount * state_tax
county_sales_tax_amount = purchase_amount * county_sales_tax
total_sales_tax = state_tax_amount + county_sales_tax_amount
total_purchase_amount = purchase_amount + total_sales_tax

print("Sale Summary:")
print("Total state tax amount:", state_tax_amount)
print("Total county sales tax amount:", county_sales_tax_amount)
print("Total sales tax:", total_sales_tax)
print("Total purchase amount:", total_purchase_amount)