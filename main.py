from inspect import CO_VARKEYWORDS
import cv2 as cv2, numpy as np, time, random
from cv2 import putText
from keras.models import load_model


# setup webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# globals
options = ['Rock', 'Paper', 'Scissors']
font = cv2.FONT_HERSHEY_SIMPLEX
color = [78,13,147]
cvline = cv2.LINE_AA
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
global game_round
global score
global game_over
global s_time
global final_toggle
global p_choice_toggle
global c_choice_toggle
global computer_choice
global player_choice
global score_added
final_toggle = False
p_choice_toggle = False
c_choice_toggle = False
score_added = False
computer_choice = "None"
# initialising
game_round = 1
score = [0,0]
game_over = False


# display the game text to keep track of score and display messages
def game_ui(frame):
    global game_round
    global score
    cv2.putText(frame, f"Player",  (10, 30), font, 1, color, 2, cvline)
    cv2.putText(frame, f"RPS-BOT", (480, 30), font, 1, color, 2, cvline)
    cv2.putText(frame, f"[{score[0]}|{score[1]}]", (280, 30), font, 1, color, 2, cvline)
    cv2.putText(frame, f"Round {game_round}",(10 , 460), font, 1, color, 2, cvline)
    # score ticks
    '''
    if score[0] >= 1:
        cv2.rectangle(frame, (,),(,), )
    if score[0] >= 2:
        cv2.rectangle(frame, (,),(,), )
    if score[0] == 3:
        cv2.rectangle(frame, (,),(,), )
    if score[0] >= 1:
        cv2.rectangle(frame, (,),(,), )
    if score[0] >= 2:
        cv2.rectangle(frame, (,),(,), )
    if score[0] == 3:
        cv2.rectangle(frame, (,),(,), color , 2, cvline)
''' 

# takes the prediction and coverts it to a gameplay option
def get_player_choice(data):
    global p_choice_toggle
    global player_choice
    #bool to lock in choice
    if p_choice_toggle == False:
        prediction = model.predict(data)
        p_choice_toggle = True
        player_choice =  options[np.argmax(prediction)]
    
def get_computer_choice():
    global c_choice_toggle
    global computer_choice
    #bool to lock in choice
    if c_choice_toggle == False:
        c_choice_toggle = True
        computer_choice = options[random.randint(0,2)]

def get_Winner(frame, user_Choice, computer_Choice):
    global game_round
    global score
    global score_added

    if user_Choice == computer_Choice and score_added == False:
        cv2.putText(frame, f"You both picked {user_Choice}, one point each!", (20, 300), font, 1, color, 2, cvline)
        score[0]+=1
        score[1]+=1
        score_added = True

    elif user_Choice == 'Rock' and computer_Choice == 'Paper' and score_added == False:
        cv2.putText(frame, f"Opponent picked {computer_Choice}! You Lose... Try Again!", (30, 300), font, 1, color, 2, cvline)
        score[1]+=1
        score_added = True

    elif user_Choice == 'Paper' and computer_Choice == 'Scissors' and score_added == False:
        cv2.putText(frame, f"Opponent picked {computer_Choice}! You Lose... Try Again!", (30, 300), font, 1, color, 2, cvline)
        score[1]+=1
        score_added = True

    elif user_Choice == 'Scissors' and computer_Choice == 'Rock' and score_added == False:
        cv2.putText(frame, f"Opponent picked {computer_Choice}! You Lose... Try Again!", (30, 300), font, 1, color, 2, cvline)
        score[1]+=1
        score_added = True

    elif score_added == False:
        cv2.putText(frame, "You Win!", (80, 110), font, 1, color, 2, cvline)
        score[0]+=1
        score_added = True

def grand_Winner(frame):
    if   score[0] >  score[1]:
        cv2.putText(frame, f"You win {score[0]} rounds to {score[1]}", (80, 110), font, 1, color, 1, cvline)
    elif score[0] == score[1]:
        cv2.putText(frame, f"you drew with {score[0]} rounds each", (80, 110), font, 1, color, 1, cvline)
    elif score[0] <  score[1]:
        cv2.putText(frame, f"you lost {score[1]} rounds to {score[0]}", (80, 110), font, 1, color, 1, cvline)
    game_over == True

def reset():
    global p_choice_toggle
    global c_choice_toggle
    global score_added

    p_choice_toggle = False
    c_choice_toggle = False
    score_added = False

###################################################################################################################
############################################ PLAY GAME ############################################################
###################################################################################################################

def play_game(g_time):
    global game_round
        
    # How many seconds each round should take, total from game initiation
    round_time = 9 * game_round

    # choice time from the end of the round
    round_choice_time = 6
    #display timer from the end of the round
    round_display_time = 3
    # seconds elapsed since code start
    e_time = time.time()-g_time

    #print ui
    game_ui(frame)
    
    #if elapsed time is greater than the rounds choice time
    if e_time < round_time - round_choice_time:
        cv2.putText(frame, f"{int(e_time)}!", (50, 200), font, 1, color, 2, cvline)
        cv2.putText(frame, f"Rock paper or scissors? {int(4-(e_time - (round_time-(9))))}!", (50, 150), font, 1, color, 2, cvline)
    elif e_time < round_time - round_display_time:
        #get the choices after the 3 second countdown
        get_player_choice(data)
        get_computer_choice()
        #display relevant information
        cv2.putText(frame, f"{player_choice}", (20, 250), font, 1 , color, 2, cvline)
        cv2.putText(frame, computer_choice, (525, 250), font, 1, color, 2, cvline)
    #if the elapsed time  is greater than the round display time
    elif e_time < round_time:
        get_Winner(frame, player_choice, computer_choice)
    elif e_time > round_time:
        reset()
        game_round +=1

        
def set_final_time(time):
    if final_toggle == False:
        final_toggle = True
        return time

###################################################################################################################
###########################################  MAIN  ################################################################
###################################################################################################################

if __name__ == "__main__":
    s_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("no Camera Found")
        # normalize the video feed to match the model data
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        
        
        # timing set-up
        e_time= time.time()
        
        # time until start
        count = e_time - s_time
        buffer = 4

        if count < buffer:            
            cv2.putText(frame, f"game will begin in {int(buffer-count)}, seconds", (30, 30), font, 1, color, 2, cvline)
        elif count > 3 and game_over == False:
            play_game(s_time+buffer)
        elif score[0] == 3 or score[1] == 3:
            grand_Winner(frame, score)
        elif game_over == True:
            final_time = set_final_time(time.time())- time.time()
            cv2.putText(frame, f"Game Over! Exiting in {3-final_time}", (250, 200), font, 1, color, 2, cvline)
            grand_Winner(frame)
            if final_time > 3:
                break
        #show the frame
        cv2.imshow('frame', frame)

        # quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(1) & 0xFF == ord('f'):
            game_over = True