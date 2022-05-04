import numpy as np
import time
import classes
options = ['Rock', 'Paper', 'Scissors', 'None']

def get_prediction(model_output):

    output_reading = np.argmax(model_output[0])
    return options[output_reading]
