try:
    number = int(input("Enter a number: "))
    for num in range(1, 11):
        print(number, "x", num, "=", number*num)
except ValueError:
    print("Please enter a number!")
