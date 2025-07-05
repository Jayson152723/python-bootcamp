hour_work = int(input("number of hours of work: "))
overtime = None
pay = None

if hour_work > 8:
    overtime = hour_work - 8
    pay = overtime * 100
    print("Your overtime pay is: ", pay)
else:
    print("You don't have overtime pay!")