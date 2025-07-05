# ask the user for the following inputs
item_1_price = float(input("Item 1 price: "))
item_2_price = float(input("Item 2 price: "))
item_3_price = float(input("Item 3 price: "))

# Print: total cost
total_cost = None
total_cost = item_1_price + item_2_price + item_3_price

print(total_cost)

item_1_qty = float(input("Item 1 qty: "))
item_2_qty = float(input("Item 2 qty: "))
item_3_qty = float(input("Item 3 qty: "))

total_qty = None
total_qty = item_1_qty + item_2_qty + item_3_qty

print(total_qty)

print("Item1 totalcost:", (item_1_qty * item_1_price))
print("Item2 totalcost:", (item_2_qty * item_2_price))
print("Item3 totalcost:", (item_3_qty * item_3_price))
print("Total Cost:", (item_1_qty * item_1_price +
                      item_2_qty * item_2_price +
                      item_3_qty * item_3_price))