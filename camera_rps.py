import cv2
import time
import random
from keras.models import load_model
import numpy as np

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Global variables
computer_wins = 0
user_wins = 0


def get_prediction_from_probabilities(probabilities):

    '''
    The function 'get_prediction_from_probabilities' finds the index of the maximum value
    in the input list of probabilities, which corresponds to the index of the predicted class, 
    and returns the name of the corresponding class as a string.

    '''
    
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

    '''
    The get_winner function takes two arguments, computer_choice and user_choice representing
    the choices of the computer and the user, respectively. It then compares the two choices to 
    determine who wins the game. The function uses the global keyword to modify the global variables 
    computer_wins and user_wins to keep track of the score.

    '''
    
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
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
