import cv2 as cv2
from keras.models import load_model
import cv2 as cv2, numpy as np
import manual_rps
import time

# setup webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# globals
font = cv2.FONT_HERSHEY_SIMPLEX
cvline = cv2.LINE_AA
color = [78,13,147]
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
buffer = 3
score = [0,0]

# encapsulated video capture function -- black camera
def vid_cap():
    ret, frame = cap.read()
    if not ret:
        print("no Camera Found")
    
    # normalize the video feed to match the model data
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    return frame, data
    

# display the game text to keep track of score and display messages
def game_ui(frame, score, round ):
    img = cv2.putText(frame, f"Player", (5, 5), font, 1, color, 1, cvline)
    img = cv2.putText(frame, f"RPS-BOT-3000", (5, 200), font, 1, color, 1, cvline)
    img = cv2.putText(frame, f"[{score[0]}|{score[1]}]", (20, 110), font, 1, color, 1, cvline)
    img = cv2.putText(frame, f"Round {round}")

# takes the prediction and coverts it to a gameplay option
def get_player_choice(data):
    options = ['Rock', 'Paper', 'Scissors', 'None']
    prediction = model.predict(data)
    return options[np.argmax(prediction)]

# display the timer during the game
def timer(frame, time):
    mins, secs = divmod(time, 60)
    timer_display = '{:02d}:{:02d}'.format(mins, secs)
    img = cv2.putText(frame, f"the game will begin in |{timer_display}|", ( 5, 100), font, 1, color, 1, cvline)


def play_game(g_time):
    rounds = 0
    while score[0] < 3 and score[1] < 3:
        e_time = time.time()-g_time
        print("here")
        frame, frame_data = vid_cap()
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
        game_ui(frame, score)
        player_choice = get_player_choice(frame_data)
        img = cv2.putText(frame, )
        if e_time > 3:
            computer_choice = manual_rps.get_computer_choice()
            manual_rps.get_Winner(frame, player_choice, computer_choice, score)
        if e_time > 6:
            rounds += 1
            continue
    manual_rps.grand_Winner(frame, score)        

if __name__ == "__main__":
    s_time = time.time()
    e_time = s_time + 1
    count = e_time - s_time
    while count <= buffer:
        e_time= time.time()
        frame, frame_data = vid_cap()
        cv2.imshow('frame', frame)
        img = cv2.putText(frame, f"game will begin in {buffer-count}, seconds", (100, 20), font, 1, color, 1, cvline)
    
    play_game(3, time.time())



'''from cv2 import imshow
from keras.models import load_model
import cv2 as cv2, numpy as np
import camera_rps, manual_rps
from time import time

options = ['Rock', 'Paper', 'Scissors', 'None']

# Load model, prep for video cap and create data array for preictive model
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# capture and normalize the image
def vidcap():
    ret, frame = cap.read()
    # normalize the video feed to match the model data
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    cv2.imshow('frame', frame)
    return data, frame

#get the prediction from the data
def get_prediction(model_output):
    return np.argmax(model_output[0])


# initialize scoreand message Counter
score  = [0,0]
init_time = int(time())


    

while True:
    #  Array of prediction data from keras model
    prediction = model.predict(data)
    
    #text box to show current prediction
    choice = manual_rps.get_user_choice(camera_rps.get_prediction(prediction))
    img  = manual_rps.frame_write(frame, f"{choice}", 1)
    
    # show the frame
    t_end = init_time + 3
    count = int(time())
    mins, secs = divmod(t_end - count, 60)
    timer_display = '{:02d}:{:02d}'.format(mins, secs)
    img = cv2.putText(frame, f"the game will begin in |{timer_display}|", ( 5, 100), font, 1, color, 1, cvline)
    
    cv2.imshow('frame', frame)
        
    while t_end < count:
        img = None
        cv2.imshow('frame', frame)
        game_Loop(init_time, camera_rps.get_prediction(prediction))
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if __name__ == "__main__":
    s_time = time.time()
    e_time = 0
    while e_time < 10:
        vidcap()
    if s_time > 10
    game_Loop()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()import cv2 as cv2
from keras.models import load_model
import cv2 as cv2, numpy as np
import manual_rps
from time import time

# globals
font = cv2.FONT_HERSHEY_SIMPLEX
cvline = cv2.LINE_AA
color = [78,13,147]
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
buffer = 3
score = [0,0]

def vid_cap():
    ret, frame = cap.read()
    # normalize the video feed to match the model data
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    cv2.imshow('frame', frame)
    return data, frame

def game_ui(frame, score, round ):
    img = cv2.putText(frame, f"Player", (5, 5), font, 1, color, 1, cvline)
    img = cv2.putText(frame, f"RPS-BOT-3000", (5, 200), font, 1, color, 1, cvline)
    img = cv2.putText(frame, f"[{score[0]}|{score[1]}]", (20, 110), font, 1, color, 1, cvline)
    img = cv2.putText(frame, f"Round {round}")

def get_player_choice(data):
    options = ['Rock', 'Paper', 'Scissors', 'None']
    prediction = model.predict(data)
    return options[np.argmax(prediction)]

def timer(frame, time):
    mins, secs = divmod(time, 60)
    timer_display = '{:02d}:{:02d}'.format(mins, secs)
    img = cv2.putText(frame, f"the game will begin in |{timer_display}|", ( 5, 100), font, 1, color, 1, cvline)


def play_game(n_rounds, time):
    rounds = 0
    while rounds < n_rounds:
        e_time = time.time()-time
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
        data, frame = vid_cap()
        game_ui(frame, score)
        player_choice = get_player_choice(data)
        img = cv2.putText(frame, )
        if e_time > 3:
            computer_choice = manual_rps.get_computer_choice()
            manual_rps.get_Winner(frame, player_choice, computer_choice, score)
        if e_time > 6:
            rounds += 1
            continue
    manual_rps.grand_Winner(frame, n_rounds, score)        

if __name__ == "__main__":
    s_time = time.time()
    e_time = s_time + 1
    count = e_time - s_time

    while count < buffer:
        e_time= time.time()
        frame, data = vid_cap()
        img = cv2.putText(frame, f"game will begin in {buffer-count}, seconds", (100, 20), font, 1, color, 1, cvline)
    
    play_game()'''