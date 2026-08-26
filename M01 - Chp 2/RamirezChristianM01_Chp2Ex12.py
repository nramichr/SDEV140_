Initial_shares_amount = 2000
share_price = 40.00
stockbroker_fee = 0.03

share_cost = Initial_shares_amount*share_price
stockbroker_fee_amount = share_cost*stockbroker_fee

print("This is the initial cost of the shares:$",f"{share_cost:.2f}")
print("This is the stockbroker fee:$",f"{stockbroker_fee_amount:.2f}")

#this is now the sold/second portion#

total_shares_sold = 2000
share_price = 42.75
additional_stockbroker_fee = 0.03

stock_amount_sold = total_shares_sold*share_price
additional_stockbroker_commission = additional_stockbroker_fee*total_shares_sold
profit = stock_amount_sold-share_cost

print("This is the amount for the sold stock:$",f"{stock_amount_sold:.2f}")
print("This is the total commissions fee for stockbroker:$",f"{additional_stockbroker_commission:.2f}")
print("This is the profit made from the transaction:$",f"{profit:.2f}")


