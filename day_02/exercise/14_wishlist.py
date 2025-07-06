import json

wishlist = [
    {
        "Name": "Car",
        "Brand": "Honda"
    },
    {
        "Name": "SUV",
        "Brand": "Toyota"
    }
]

for order in wishlist:
    print("Item: ")
    for key, value in order.items():
        print("\t", key, value)


with open('wishlist.json', 'w') as file:
    json.dump(wishlist, file, indent = 4)