import numpy as np
import time
import classes
options = ['Rock', 'Paper', 'Scissors', 'None']

def get_prediction(frame, model_output):
    start = time.time()
    count = start-time.time()
    output_reading = np.argmax(model_output[0])
    count_down = classes.TextBox(frame, f"{count}")

    if (count == start+3):
        return options[output_reading]
        count_down.remove()
    else:
        count_down.write()
