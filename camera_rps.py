import cv2
import numpy as np
import time
options = ['Rock', 'Paper', 'Scissors', 'None']
font = cv2.FONT_HERSHEY_SIMPLEX
colour = (147, 101, 26)

def get_prediction(frame, model_output):
    start = int(time.time())
    count = int(start-time.time())
    end = int(start+3)
    text = f"You is showing {options[output_reading]}"
    img = cv2.putText(frame, text, (50,50), font, 1, colour, 2, cv2.LINE_AA)
    
    if (count == end):
        output_reading = np.argmax(model_output[0])
        return options[output_reading]
    else:
        countdown_text = f"{count}"
        img = cv2.putText(frame, countdown_text, (50, 150), font,  1, colour, 2, cv2.LINE_AA )