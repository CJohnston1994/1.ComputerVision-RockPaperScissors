import cv2 as cv2
from keras.models import load_model
import numpy as np
import camera_rps
import manual_rps
import classes
from time import sleep

model = load_model('Res/keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    
    show_choice = classes.TextBox(frame, f"You are showing {camera_rps.get_prediction(frame, prediction)}")
    show_choice.write()
    cv2.imshow('frame', frame)

    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        show_choice.remove()
        sleep(5)
        break
        
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        manual_rps.play(camera_rps.get_prediction(frame, prediction))
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()