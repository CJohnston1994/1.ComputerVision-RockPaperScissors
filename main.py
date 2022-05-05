from keras.models import load_model
import cv2 as cv2, numpy as np
import math, camera_rps, manual_rps
from classes import TextBox
from time import time

# Load model, prep for video cap and create data array for preictive model
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# number of rounds
best_of = 3

# initialize scoreand message Counter
score  = [0,0]

def game_Loop():
    '''game_timer = timer - time()
    round_count  = 0
    while round_count < best_of:
        start = int(time())
        while timer < 3:
            print("also Got  Here!")
            count_down_timer = TextBox(frame, f"count",3)
            img = count_down_timer.write()
        user_Choice = manual_rps.get_user_choice(prediction)
        computer_Choice  = manual_rps.get_computer_choice()
        manual_rps.get_Winner(user_Choice, computer_Choice, score)
    manual_rps.grand_Winner()'''
    return

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    
    #  Array of prediction data for rps options
    prediction = model.predict(data)
    
    #text box to show current prediction
    begin = TextBox(frame, "Press \'s\' to begin the game", 1)
    img  = begin.write()
    
    # show the frame
    cv2.imshow('frame', frame)

    #Begin  the game
    game_Loop()
    manual_rps.grand_Winner(frame, best_of, score)

    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        begin.remove()
        t_end = int(time()) + 10
        count = int(math.floor(time()))
        timertext = f"{divmod(60, count-time())}"
        TimerTxt = TextBox(frame, timertext, 1)
        print(count)
        if t_end > count:
            TimerTxt.write()
        else:
            game_Loop()



# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()