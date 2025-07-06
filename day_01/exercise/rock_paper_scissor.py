from random import choice

user_choice = input("Pick a choice (rock/paper/scissor): ")
print(user_choice)
options = ["rock", "paper", "scissors"]
random_option = choice(options)
print(random_option)

def player_rock(user_choice, random_choice):
    if user_choice == "rock" and random_option == "scissor":
        print("Player win!")
    elif user_choice == "paper" and random_option == "rock":
        print("Player win!")
    elif user_choice == "scissor" and random_option == "paper":
        print("Player wins!")

