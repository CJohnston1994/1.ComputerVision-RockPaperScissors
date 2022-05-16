import cv2 as cv2, numpy as np, time, random
from cv2 import putText
from keras.models import load_model


# setup webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

#used throughout
options = ['Rock', 'Paper', 'Scissors']
font = cv2.FONT_HERSHEY_SIMPLEX
color = [78,13,147]
cvline = cv2.LINE_AA
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# globals
global game_round
global score
global game_over
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
# initialising
game_round = 1
score = [0,0]
game_over = False


# display the game text to keep track of score and display messages
def game_ui(frame, game_round):
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

def get_Winner(frame, user_Choice, computer_Choice, score):
    global game_round
    global score_added

    if user_Choice == computer_Choice:
        cv2.putText(frame, f"You both picked {user_Choice}!", (150, 250), font, 1, color, 2, cvline)
        cv2.putText(frame, f"one point each!", (200, 300), font, 1, color, 2, cvline)

        if score_added == False:
            score[0]+=1
            score[1]+=1
            return score          
    elif user_Choice == 'Rock' and computer_Choice == 'Paper':
        cv2.putText(frame, f"Opponent picked {computer_Choice}!", (150, 250), font, 1, color, 2, cvline)
        cv2.putText(frame, f"You Lose... Try Again!", (200, 300), font, 1, color, 2, cvline)

        if score_added == False:
            score[1]+=1            
    elif user_Choice == 'Paper' and computer_Choice == 'Scissors':
        cv2.putText(frame, f"Opponent picked {computer_Choice}!", (150, 250), font, 1, color, 2, cvline)
        cv2.putText(frame, f"You Lose... Try Again!", (200, 300), font, 1, color, 2, cvline)
        if score_added == False:
            score[1]+=1            
    elif user_Choice == 'Scissors' and computer_Choice == 'Rock':
        cv2.putText(frame, f"Opponent picked {computer_Choice}!", (150, 250), font, 1, color, 2, cvline)
        cv2.putText(frame, f"You Lose... Try Again!", (200, 300), font, 1, color, 2, cvline)        
        if score_added == False:
            score[1]+=1            
    else:
        cv2.putText(frame, f"Opponent picked{computer_Choice} You Win!", (80, 110), font, 1, color, 2, cvline)
        if score_added == False:
            score[0]+=1
    score_added = True
            
def grand_Winner(frame):
    global score
    if   score[0] >  score[1]:
        cv2.putText(frame, f"You win {score[0]} rounds to {score[1]}", (80, 110), font, 1, color,2, cvline)
    elif score[0] == score[1]:
        cv2.putText(frame, f"you drew with {score[0]} rounds each", (80, 110), font, 1, color, 2, cvline)
    elif score[0] <  score[1]:
        cv2.putText(frame, f"you lost {score[1]} rounds to {score[0]}", (80, 110), font, 1, color, 2, cvline)

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
    global game_over
        
    # How many seconds each round should take, total from game initiation
    round_time = 9 * game_round

    # choice time from the end of the round
    round_choice_time = 6
    #display timer from the end of the round
    round_display_time = 3
    # seconds elapsed since code start
    elapsed_time = time.time()- g_time

    #print ui
    game_ui(frame, game_round)
    #leave the function if either player has 3 points    
    if score[0] == 3 or score[1] == 3:
        grand_Winner(frame)
        game_over = True
        return
    #if elapsed time is greater than the rounds choice time
    if elapsed_time < round_time - round_choice_time:
        cv2.putText(frame, f"{int(elapsed_time)}!", (50, 200), font, 1, color, 2, cvline)
        cv2.putText(frame, f"Rock paper or scissors? {int(4-(elapsed_time - (round_time-(9))))}!", (50, 150), font, 1, color, 2, cvline)
    elif elapsed_time < round_time - round_display_time:
        #get the choices after the 3 second countdown
        get_player_choice(data)
        get_computer_choice()
        #display relevant information
        cv2.putText(frame, f"{player_choice}", (20, 250), font, 1 , color, 2, cvline)
        cv2.putText(frame, computer_choice, (525, 250), font, 1, color, 2, cvline)
    #if the elapsed time  is greater than the round display time
    elif elapsed_time < round_time:
        get_Winner(frame, player_choice, computer_choice)
    elif elapsed_time > round_time:
        reset()
        game_round +=1

        
def set_game_ending():
    global final_toggle
    if final_toggle == False:
        final_toggle = True
        return time.time()+4


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
        elif game_over == True:
            final_time = set_game_ending(time.time())
            if final_time < time.time():
                cv2.putText(frame, f"Game Over! Exiting in {4-final_time}", (250, 200), font, 1, color, 2, cvline)
            else:
                break
        #show the frame
        cv2.imshow('frame', frame)

        # quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(1) & 0xFF == ord('f'):
            game_over = True