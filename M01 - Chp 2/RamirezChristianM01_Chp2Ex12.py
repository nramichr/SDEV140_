Initial_shares_amount = 2000
share_price = 40.00
stockbroker_fee = 0.03

share_cost = Initial_shares_amount * share_price
stockbroker_fee_amount = share_cost * stockbroker_fee
print("This is the initial cost of the shares: $",f"{share_cost:.2f}")
print("This is the stockbroker fee: $",f"{stockbroker_fee_amount:.2f}")


shares_sold = 2000
share_price = 42.75
additional_stockbroker_fee = 0.03

