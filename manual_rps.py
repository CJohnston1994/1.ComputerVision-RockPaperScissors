# function for  rock paper scissors
import random

options = ['Rock', 'Paper', 'Scissors']

def get_user_choice():
    choice = input("Rock, paper or scissors? ")
    if choice.capitalize() in options:
        return choice.capitalize()
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

def play():
    user_Choice = get_user_choice()
    computer_Choice  = get_computer_choice()
    get_Winner(user_Choice, computer_Choice)

play()
