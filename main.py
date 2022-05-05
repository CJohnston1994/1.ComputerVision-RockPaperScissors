import cv2 as cv2
from keras.models import load_model
import numpy as np
import camera_rps
import manual_rps
from classes import TextBox
from time import time

# Load model, prep for video cap and create data array for preictive model
model = load_model('Res/keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# number of rounds
best_of = 3

# initialize score
score  = [0,0]

def game_Loop():
    while best_of not in range(best_of, 0, -1):
        start = int(time())
        while count_down < 3 :
            print("also Got  Here!")
            count_down  = int(3 - (start - time()))
            count_down_timer = TextBox(frame, f"count")
            img = count_down_timer.write()

            if count_down < 3:
                user_Choice = manual_rps.get_user_choice(prediction)
                computer_Choice  = manual_rps.get_computer_choice()
                manual_rps.get_Winner(user_Choice, computer_Choice, score)
                False
            else: 
                continue


while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    
    #  Array of prediction data for rps options
    prediction = model.predict(data)
    
    #text box to show current prediction
    show_choice = TextBox(frame, f"You are showing {camera_rps.get_prediction(prediction)}")
    img = show_choice.write()
    test1 = TextBox(frame,  "test text, check for line 2")
    img  = test1.write()
    
    # show the frame
    cv2.imshow('frame', frame)

    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #Begin  the game
    game_Loop()
    manual_rps.grand_Winner(frame, best_of, score)

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()