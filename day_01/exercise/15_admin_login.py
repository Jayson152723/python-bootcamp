correct_username = "admin"
correct_password = "admin"

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if correct_username == username_input and correct_password == password_input:
    print("Access granted!")
else:
    print("Access denied!")
