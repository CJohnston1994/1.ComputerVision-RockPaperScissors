# function for  rock paper scissors
from typing import Text
import random
import cv2 as cv2

font = cv2.FONT_HERSHEY_SIMPLEX
cvline = cv2.LINE_AA
color = [78,13,147]

options = ['Rock', 'Paper', 'Scissors']

def get_user_choice(prediction):
    #choice = input("Rock, paper or scissors? ")
    return options[prediction]
    
def get_computer_choice():
    roll = random.randint(0,2)
    ai_choice = options[roll]
    return ai_choice

def get_Winner(frame, user_Choice, computer_Choice, score):
    if user_Choice == computer_Choice:
        img = cv2.putText(frame, f"You both picked {user_Choice}", (80, 110), font, 1, color, 1, cvline)
        return [score[0]+1,score[1]+1]
    elif user_Choice == 'Rock' and computer_Choice == 'Paper':
        img = cv2.putText(frame, "Opponent picked {computer_Choice}! You Lose... Try Again!", (40, 110), font, 1, color, 1, cvline)
        return [score[0],score[1]+1]
    elif user_Choice == 'Paper' and computer_Choice == 'Scissors':
        img = cv2.putText(frame, "Opponent picked {computer_Choice}! You Lose... Try Again!", (40, 110), font, 1, color, 1, cvline)
        return [score[0],score[1]+1]
    elif user_Choice == 'Scissors' and computer_Choice == 'Rock':
        img = cv2.putText(frame, "Opponent picked {computer_Choice}! You Lose... Try Again!", (40, 110), font, 1, color, 1, cvline)
        return [score[0],score[1]+1]
    else:
        img = cv2.putText(frame, "You Win!", (80, 110), font, 1, color, 1, cvline)
        return [score[0]+1,score[1]]

def grand_Winner(frame, best_of, score):
    if   best_of == 0 and score[0] >  score[1]:
        img = cv2.putText(frame, f"You win {score[0]} rounds to {score[1]}", (80, 110), font, 1, color, 1, cvline)
    elif best_of == 0 and score[0] == score[1]:
        img = cv2.putText(frame, f"you drew with {score[0]} rounds each", (80, 110), font, 1, color, 1, cvline)
    elif best_of == 0 and score[0] <  score[1]:
        img = cv2.putText(frame, f"you lost {score[1]} rounds to {score[0]}", (80, 110), font, 1, color, 1, cvline)
