item_count = int(input("Enter item count: "))
total = 0

for item in range(item_count):
    item_qty = int(input("Enter quantity: "))
    item_price = int(input("Enter item price: "))
    total = total + item_price*item_qty

print("Total cost: " + str(total))

