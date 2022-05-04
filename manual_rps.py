# function for  rock paper scissors
from typing import Text
from classes import TextBox
import random
from time  import time

options = ['Rock', 'Paper', 'Scissors']

def get_user_choice(prediction):
    #choice = input("Rock, paper or scissors? ")
    start_time = time.time()
    
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
    if best_of == 0 and score[0]>score[1]:
        you_win = TextBox(frame, f"you won {score[0]} to {score[1]}")
    if best_of == 0 and score[0]>score[1]:
        you_draw = TextBox(frame, f"you drew with {score[0]} points each")
    if best_of == 0 and score[0]>score[1]:
        you_lose = TextBox(frame, f"you lost {score[1]} to {score[0]}")

def intro(frame):
    intro_box1= TextBox(frame, "Welcome to Rock, Paper... Scissors!")
    intro_box2= TextBox(frame, "Can you beat the most sophistocated AI Imaginabl?")
    intro_box3= TextBox(frame, "Muahahahahahahaha")

    intro_box1.write()
    intro_box2.write()
    intro_box3.write()


