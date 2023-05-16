import random

def get_computer_choice():

    '''
    The function get_computer_choice chooses randomly a string from the rps_list and then return the 
    computer choice.
    '''
    rps_list =['rock', 'paper', 'scissors']
    computer_choice = random.choice(rps_list)
    return computer_choice

def get_user_choice():

    '''
    The function get_user_choice asks the user's to input their move: rock, paper or scissors.
    It is nested in a while validation loop to make sure the user inputs a valid move for the game. 
    If the user_choice is not in the strings given, then it prints a statement to try again.
    '''
    valid_input = False 
    while not valid_input:
        user_choice = input("rock, paper or scissors:").lower()
        if user_choice not in('rock', 'paper', 'scissors'):
            print("Invalid input! Please choose a move by typing either rock, paper or scissors.")
        else:
            return user_choice

def get_winner(computer_choice, user_choice):

    '''
    The get_winner function takes two arguments, computer_choice and user_choice representing
    the choices of the computer and the user, respectively. It then compares the two choices to 
    determine who wins the game. 

    '''
    

    if user_choice == computer_choice:
            print("Tie!")
            return 'tie'
    elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("Computer lost! You won!")
            return 'user'
    else:
            print("You lost! Computer won!!")
            return 'computer'


def play():
    '''
    The play function represents the main logic of the game. It initializes a variable count to keep 
    track of the number of rounds played. Within each iteration of the loop, it increments the count 
    by 1 to keep track of the number of rounds played. After each round, it checks if count is equal 
    to 5. If so, it asks the user if they want to continue playing by prompting "Do you want to 
    continue? (y/n):". If the user's response is not 'y', the loop is broken, and the game ends. 
    Otherwise, if the user's response is 'y' (yes), it resets the count to 0, and the loop continues 
    for the next set of rounds.
    '''
    count = 0
    computer_wins = 0
    user_wins = 0

    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        winner = get_winner(computer_choice, user_choice)

        if winner == 'computer':
            computer_wins += 1
        elif winner == 'user':
            user_wins += 1

        count += 1

        if count == 5:
            print(f"Score: Computer {computer_wins} - {user_wins} User")
            while True:
                play_again = input("Do you want to continue? (y/n): ").lower()
                if play_again == 'y':
                    count = 0
                    break
                elif play_again == 'n':
                    if computer_wins > user_wins:
                        print("Computer won the game!")
                    elif user_wins > computer_wins:
                        print("You won the game!")
                    else:
                        print("It's a tie!")
                    return
                else:
                    print("Invalid input! Please choose 'y' to continue or 'n' to exit.")

play()




