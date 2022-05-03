from cv2 import putText
from cv2 import FONT_HERSHEY_SIMPLEX, LINE_AA

class TextBox:
    _counter = 0
    font = FONT_HERSHEY_SIMPLEX
    colour = (147, 101, 26)

    def __init__(self, frame, text):
        TextBox._counter+=1
        self.frame = frame
        self.text = text
        
    def write(self):
        img = putText(self.frame, self.text, (50, 50*TextBox._counter), self.font,  1, self.colour, 2, LINE_AA )

    def remove(self,frame):
        del self
        TextBox._counter -= 1