# tax calculator

#get price and tax
price = float(input("Please enter the price of the item: "))
tax_rate = float(input("Please enter the tax rate as a decimal: "))

#calculate and display tax
print(f"Price: ${price:.2f}")
tax_cost = price * tax_rate
print(f"Tax: ${tax_cost:.2f}")

# calculate and display total cost
total_cost = price + tax_cost
print(f"Total Cost: ${total_cost:.2f}")