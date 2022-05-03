import cv2 as cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
options = ['Rock', 'Paper', 'Scissors','None']

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, dsize=(224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    text = f"Player is showing {options[max]}, press \'l\' to  lock in "
    img = cv2.putText(frame, text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (147, 101, 26), 3, cv2.LINE_AA)    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
