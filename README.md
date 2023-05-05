# Computer Vision RPS
This project uses machine learning and specifically the library tensorflow, keras to train the model based ont the captured images taken from teachable machine for the game computer-vision-rock-paper-scissors.

# Milestone_1
In Milestone_1, a repository was created in github in order to track the changes in the code. 

# Milestone_2
In Milestone_2 by using Teachable-Machine, multiple images was taken for rock-paper-scirros movements, in order to train the model as precise as possible. After the training of the model, the model was downloaded and the changes was pushed to the git repository.

# Milestone_3
In Milestone_3, firstly a conda environment was created called my_env, then it followed the activation of the environment and then the command pip installed in order to install the necessary requirements such as opencv-python, tensorflow and ipykernel. Afterwards, the model downloaded from the provided link was checked to make sure that everything was working perfectly and familiarising with the code.

''' 

The following commands have been used in order, to install the libraries mentioned above:

conda create -n my_env python = 3.8
conda pip install
pip install
 
 
 '''

 # Milestone_4
In Milestone_4, a file created called manual_rps.py which stores the users and compters choices along with two functions called get_computer_choice and get_user_choice. The function get_computer_choice choose randomly between rock-paper-scissors and the function get_user_choice, its asking the user to choose between rock-paper-scissors, nested in while validation loop to make sure the user enter the correct input. Last but not least, the winner function created taking as arguments the computer_choice and user_choice to figure out who won. This function is consisting of if-elif-else statements. Lastly,the play function created to simulate the game, consisting of a while loop set to True, calling the functions get_computer_choice, get_user_choice and get_winner. Also the variable count defined to count the rounds played and asks the users if they want to play again after every 3 rounds. If the user enters 'y', the count is reset to 0 and the game continues. If the user enters anything else, the loop is broken and the game ends.

''' 



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




'''

# Milestone_5
In milestone_5, a file created called camera_rps.py and putting everything together to create the logic of the game. Also, the function get_prediction_from_probabilities created which finds the index of the maximum value in the input list of probabilities. Then, function time was imported in order to get how much time has passed since the the script started. The get_winner function added with an update such as including the global variables user_wins and computers_wins to assist in counting the rounds of victory for the computer and the user.

''' 

Global variables
computer_wins = 0
user_wins = 0


def get_prediction_from_probabilities(probabilities):

    '''The function 'get_prediction_from_probabilities' finds the index of the maximum value
       in the input list of probabilities, which corresponds to the index of the predicted class, 
       and returns the name of the corresponding class as a string.'''
    
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

    '''The get_winner function takes two arguments, computer_choice and user_choice representing
      the choices of the computer and the user, respectively. It then compares the two choices to 
      determine who wins the game. The function uses the global keyword to modify the global variables 
      computer_wins and user_wins to keep track of the score.'''
    
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

while True:
    
      '''
    The while loop implements the main logic of the game. 
    It runs continuously until a player has won three rounds, or the user chooses to quit.
    On each iteration of the loop, the program prompts the user to show their hand and captures
    a video frame using the computer's camera. It then resizes and normalizes the frame to prepare
    it for input into a pre-trained machine learning model. 
    The model predicts the most likely hand gesture shown by the user, and the program selects a random
    choice for the computer player. It then compares the choices to determine the winner of the round 
    using the get_winner function.
    The program keeps track of the rounds won by the user and the computer, once the player has won 
    3 rounds, the program announces the winner and terminates the game.
    
    ''' 

    countdown = 3
    start_time = time.time()
    while countdown > 0:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 1.0:
            print(countdown)
            countdown -= 1
            start_time = time.time()
        # Wait for a short time between each count
        cv2.waitKey(100)
    print("Show your hand!")

    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    user_choice = get_prediction_from_probabilities(prediction)
    print(f"Computer chose {computer_choice}")
    print(f"You chose {user_choice}")
    get_winner(computer_choice, user_choice)
    if computer_wins == 3:
        print("Computer won the game!")
        break
    elif user_wins == 3:
        print("You won the game!")
        break
    cv2.imshow('frame', frame)
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
After the loop release the cap object
cap.release()
Destroy all the windows
cv2.destroyAllWindows()


'''

# Conclusion
In conclusion, this project has allowed me to gain a better understanding of machine learning concepts and the numpy library. I have also improved my skills in implementing while loops and if-else statements, as well as organizing code in a logical order. Moving forward, there is potential for further improvement by implementing classes to enhance the code structure and readability. Additionally, adding an option for the user to choose whether or not to play another game would enhance the overall user experience



