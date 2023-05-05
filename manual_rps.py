import random

def get_computer_choice():
    rps_list =['rock', 'paper', 'scissors']
    computer_choice = random.choice(rps_list)
    return computer_choice

def get_user_choice():
    valid_input = False
    while not valid_input:
        user_choice = input("rock, paper or scissors:").lower()
        if user_choice not in('rock', 'paper', 'scissors'):
            print("Invalid input! Try entering a string.")
        else:
            return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You won!")
    else:
        print("You lost! Computer won!")

def play():
    count = 0
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        winner = get_winner(computer_choice, user_choice)
        count += 1
        if count == 3:
            play_again = input("Do you want to continue? (y/n): ").lower()
            if play_again != 'y':
                break
            else:
                count = 0

play()