from cv2 import putText
from cv2 import FONT_HERSHEY_SIMPLEX, LINE_AA

class TextBox:
    _counter = 0
    font = FONT_HERSHEY_SIMPLEX
    colour = (147, 101, 26)

    def __init__(self, frame, text):
        TextBox._counter+=1
        self.counter = TextBox._counter 
        self.text = text
        self.frame = frame
    
    def __del__(self):
        TextBox._counter -=1

    def write(self):
        
        img = putText(self.frame, self.text, (50, 50*self.counter), self.font,  1, self.colour, 2, LINE_AA )