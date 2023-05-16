# **Computer Vision RPS**
This project uses machine learning and specifically the library tensorflow, keras to train the model based on the captured images taken from teachable machine for the game computer-vision-rock-paper-scissors.

### **Milestone 1**
A repository was created in github in order to track the changes in the code. 

### **Milestone 2**
By using Teachable-Machine, multiple images were taken for rock, paper and scissors movements, in order to train the model precisely. After the training of the model, the model was downloaded and the changes were pushed to the git repository.

### **Milestone 3**
Firstly, a conda environment was created named `my_env`. After activating the
environment, the necessary packages such as opencv-python, tensorflow and ipykernel were
installed. Afterwards, the `RPS_template.py` file was run to check that the model trained in
Teachable Machine was working perfectly before the game logic was implemented.

The following commands have been used in order, to install the libraries mentioned above:

```
conda create -n my_env python = 3.8
conda pip install
pip install

```


### **Milestone 4**
A file was created named manual_rps.py which stores the user's and computer's choices along with two functions named `get_computer_choice` and `get_user_choice`. The function `get_computer_choice` chooses randomly between rock, paper and scissors. The function `get_user_choice` asks the user to type their chosen move: rock, paper and scissors. It is nested in a while validation loop to make sure the user inputs a valid move for the game. Last but not least, the `get_winner` function takes as arguments the `computer_choice` and `user_choice` to determie the winner. This function consists of conditional statements. The `play` function was implemented to simulate the game, consisting of a while loop set to True, calling the functions `get_computer_choice`, `get_user_choice` and `get_winner`. Lastly, the variable count is defined to count the rounds played and asks the users if they want to play again after every 3 rounds. If the user enters 'y', the count is reset to 0 and the game continues. If the user enters anything else, the loop is broken and the game ends.

```

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

```

### **Milestone 5**
A file named `camera_rps.py` was created to consolidate all the game logic The `get_prediction_from_probabilities` function was implemented to find the index of the maximum value in a list of probabilities. Additionally, the `time` function was imported to track the script's execution time. To enhance the `get_winner` function, global variables `user_wins` and `computers_wins` were incorporated to keep count of the number of victories for both the computer and the user.

 
```
def get_prediction_from_probabilities(probabilities):

    'The function 'get_prediction_from_probabilities' finds the index of the maximum value
       in the input list of probabilities, which corresponds to the index of the predicted class, 
       and returns the name of the corresponding class as a string.'
    
    predicted_class = probabilities.argmax()
    if predicted_class == 0:
        return "rock"
    elif predicted_class == 1:
        return "paper"
    elif predicted_class == 2:
        return "scissors"
    else:
        return "neutral"

def get_winner(computer_choice, user_choice):

    'The get_winner function takes two arguments, computer_choice and user_choice representing
      the choices of the computer and the user, respectively. It then compares the two choices to 
      determine who wins the game. The function uses the global keyword to modify the global variables 
      computer_wins and user_wins to keep track of the score.'
    
    global computer_wins, user_wins 
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("Computer lost! You won!")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("Computer lost! You won!")
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Computer lost! You won!")
        user_wins += 1
    else:
        print("You lost! Computer won!!")
        computer_wins += 1
```


## **Conclusion**
In conclusion, this project has allowed me to gain a better understanding of machine learning concepts and the numpy library. I have also improved my skills in implementing while loops and if-else statements, as well as organizing code in a logical order. Moving forward, there is potential for further improvement by implementing classes to enhance the code structure and readability. Additionally, adding an option for the user to choose whether or not to play another game would enhance the overall user experience.