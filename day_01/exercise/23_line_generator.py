number = int(input("Enter a number: "))
message = input("Enter message: ")

def line_generator(message = "Line", number = 3):
    for num in range(1, number + 1):
        print(message, num)

line_generator(message, number)
