# function for  rock paper scissors
import random
import time

options = ['Rock', 'Paper', 'Scissors']

def get_user_choice(prediction):
    #choice = input("Rock, paper or scissors? ")
    start_time = time.time()
    
    if prediction != 'None':
        return prediction
    else:
        print('please try again')
        get_user_choice()

def get_computer_choice():
    roll = random.randint(0,2)
    ai_choice = options[roll]
    return ai_choice

def get_Winner(user_Choice, computer_Choice):
    if user_Choice == computer_Choice:
        print("draw")
    elif user_Choice == 'Rock' and computer_Choice == 'Paper':
        print("You Lose... Try Again!")
    elif user_Choice == 'Paper' and computer_Choice == 'Scissors':
        print("You Lose... Try Again!")
    elif user_Choice == 'Scissors' and computer_Choice == 'Rock':
        print("You Lose... Try Again!")
    else:
        print('You Win')

def play(prediction):
    user_Choice = get_user_choice(prediction)
    computer_Choice  = get_computer_choice()
    get_Winner(user_Choice, computer_Choice)