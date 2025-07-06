user_input = input("Enter number: ").strip().replace(",","")
all_numeric = user_input.isnumeric()

if all_numeric:
    user_input = int(user_input)
    print(user_input + 1)
else:
    print("Please enter a valid number!")