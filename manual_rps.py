# function for  rock paper scissors
from typing import Text
from classes import TextBox
import random

options = ['Rock', 'Paper', 'Scissors']

def get_user_choice(prediction):
    #choice = input("Rock, paper or scissors? ")
    
    if prediction != 'None':
        return options[prediction]
    else:
        print('please try again')
        get_user_choice()

def get_computer_choice():
    roll = random.randint(0,2)
    ai_choice = options[roll]
    return ai_choice

def get_Winner(user_Choice, computer_Choice, score):
    if user_Choice == computer_Choice:
        print("draw")
        return [score[0]+1,score[1]+1]
    elif user_Choice == 'Rock' and computer_Choice == 'Paper':
        print("You Lose... Try Again!")
        return [score[0],score[1]+1]
    elif user_Choice == 'Paper' and computer_Choice == 'Scissors':
        print("You Lose... Try Again!")
        return [score[0],score[1]+1]
    elif user_Choice == 'Scissors' and computer_Choice == 'Rock':
        print("You Lose... Try Again!")
        return [score[0],score[1]+1]
    else:
        print('You Win')
        return [score[0]+1,score[1]]

def grand_Winner(frame, best_of, score):
    if best_of == 0 and score[0] > score[1]:
        img = TextBox(frame, f"you won {score[0]} to {score[1]}").write()
    elif best_of == 0 and score[0] == score[1]:
        img = TextBox(frame, f"you drew with {score[0]} points each")
    else:
        img = TextBox(frame, f"you lost {score[1]} to {score[0]}")
