from xml.etree.ElementTree import indent

import json

wishlist = [
    {'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer'},
    {'Name': 'Bob', 'Age': 25, 'Occupation': 'Designer'},
]
with open('people.json', 'w') as file:
    json.dump(data, file, indent = 4)