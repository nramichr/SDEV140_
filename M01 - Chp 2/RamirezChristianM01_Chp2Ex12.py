"""
      12.
      Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:The number of shares that Joe purchased was 2,000.
      When Joe purchased the stock, he paid $40.00 per share.  Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid for
      the stock.Two weeks later, Joe sold the stock. Here are the details of the sale:The number of shares that Joe sold was 2,000.
      He sold the stock for $42.75 per share.  He paid his stockbroker another commission that amounted to 3 percent of the amount
      he received for the stock.Write a program that displays the following information: The amount of money Joe paid for the stock.
      The amount of commission Joe paid his broker when he bought the stock.  The amount for which Joe sold the stock.
      The amount of commission Joe paid his broker when he sold the stock.  Display the amount of money that Joe had left when he
      sold the stock and paid his broker (both times). If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.
"""


INITIAL_SHARES_AMOUNT = 2000
SHARE_PRICE = 40.00
STOCKBROKER_FEE = 0.03

share_cost = INITIAL_SHARES_AMOUNT*SHARE_PRICE
stockbroker_fee_amount = share_cost*STOCKBROKER_FEE

print("This is the initial cost of the shares:$",f"{share_cost:,.2f}")
print("This is the stockbroker fee:$",f"{stockbroker_fee_amount:,.2f}")

#this is now the sold/second portion

TOTAL_SHARES_SOLD = 2000
SHARE_PRICE = 42.75
ADDITIONAL_STOCKBROKER_FEE = 0.03

stock_amount_sold = TOTAL_SHARES_SOLD*SHARE_PRICE
additional_stockbroker_commission = ADDITIONAL_STOCKBROKER_FEE*TOTAL_SHARES_SOLD
expenses = additional_stockbroker_commission-stockbroker_fee_amount

profit = stock_amount_sold-share_cost

print("This is the amount for the sold stock:$",f"{stock_amount_sold:,.2f}")
print("This is the total commissions fee for stockbroker:$",f"{additional_stockbroker_commission:,.2f}")
print("This is the profit made from the transaction:$",f"{profit+expenses:,.2f}")

print("Christian Ramirez-Flores")