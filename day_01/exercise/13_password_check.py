correct_password = "pass"

password_input = input("Please provide password: ")

correct_password_given = None

correct_password_given = correct_password == password_input

if  correct_password_given:
    print("Access granted!")
else:
    print("Access denied!")
