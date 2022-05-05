from keras.models import load_model
import cv2 as cv2, numpy as np
import camera_rps, manual_rps
from time import time

# Load model, prep for video cap and create data array for preictive model
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# number of rounds
best_of = 3

# initialize scoreand message Counter
score  = [0,0]

def frame_write(frame, text, message_height):
    img = cv2.putText(frame, text, (50, 50*message_height), cv2.FONT_HERSHEY_SIMPLEX,  1, (147, 101, 26), 2, cv2.LINE_AA )

def game_Loop():
    '''game_timer = timer - time()
    round_count  = 0
    while round_count < best_of:
        start = int(time())
        while timer < 3:
            print("also Got  Here!")
            count_down_timer = frame_write(frame, f"count",3)
            img = count_down_timer
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
    img  = frame_write(frame, "Press \'s\' to begin the game", 1)
    
    # show the frame
    int_time = int(time())
    t_end = int_time + 10
    count = int_time
    mins, secs = divmod(t_end - count, 60)
    timer_display = '{:02d}:{:02d}'.format(mins, secs)
  
    img = frame_write(frame, f"{timer_display}", 2)
    
    cv2.imshow('frame', frame)
    
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()