from cv2 import putText
from cv2 import FONT_HERSHEY_SIMPLEX, LINE_AA

class TextBox:
    font = FONT_HERSHEY_SIMPLEX
    colour = (147, 101, 26)

    def __init__(self, frame, text, message_height): 
        self.text = text
        self.frame = frame
        self.message_height = message_height
    
    def write(self):
        img = putText(self.frame, self.text, (50, 50*self.message_height), self.font,  1, self.colour, 2, LINE_AA )
        
    def remove(self):
        del self