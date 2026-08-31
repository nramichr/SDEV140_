"""
A software company sells a package that retails for $99. Quantity discounts are given according to the following 
+-------------+---------+
|Quantity     |Discount |
+-------------+---------+
| 10~19       | 10%     |
| 20~49       | 20%     |
| 50~99       | 30%     |
| 100 or more | 40%     |
+-------------+---------+

Write a program that asks the user to enter the number of packages purchased. 
The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.
"""

def main():
    packages_purchased: int = int(input("Enter number of packages purchased: "))
    PACKAGE_PRICE: int = 99

    if packages_purchased >= 100:
        discount = 0.4
    elif packages_purchased >= 50 and packages_purchased <= 99:
        discount = 0.3
    elif packages_purchased >= 20 and packages_purchased <= 49:
        discount = 0.2
    elif packages_purchased >= 10 and packages_purchased <= 19:
        discount = 0.1
    else:
        discount = 0

    total_cost = packages_purchased * PACKAGE_PRICE
    discount_amount = total_cost * discount
    final_cost = total_cost - discount_amount

    print(f"Discount: ${discount_amount:,.2f}")
    print(f"Total cost after discount: ${final_cost:,.2f}")
main()

print('Christian Ramirez Flores')