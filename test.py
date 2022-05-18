from typing import final
import cv2, numpy as np, time
from random import randint
from keras.models import load_model

# Data
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Design
font = cv2.FONT_HERSHEY_SIMPLEX
color = [78,13,147]
cvline = cv2.LINE_AA

class Game:
    def __init__(self):
        self.score = [0,0]
        self.options = ["Rock", "Paper", "Scissors", "None"]
        self.game_round = 1
        self.player_choice = "Test"
        self.computer_choice = "Test"
        self.flag_c_choice = False
        self.flag_p_choice = False
        self.flag_score = False
        self.flag_final = False
        self.start_time = time.time()
        self.round_length = 12

    def game_UI(self, frame):
        elapsed_time = int(time.time() - self.start_time)
        cv2.putText(frame, f"Player",  (10, 30), font, 1, color, 2, cvline)
        cv2.putText(frame, f"RPS-BOT", (480, 30), font, 1, color, 2, cvline)
        cv2.putText(frame, f"[{self.score[0]}|{self.score[1]}]", (280, 30), font, 1, color, 2, cvline)
        cv2.putText(frame, f"Round {self.game_round}",(10 , 460), font, 1, color, 2, cvline)
        cv2.putText(frame, f"{elapsed_time})",(10 , 420), font, 1, color, 2, cvline)
        # score ticks
        '''
        if score[0] >= 1:
            cv2.rectangle(frame, (,),(,), )
        if score[0] >= 2:
            cv2.rectangle(frame, (,),(,), )
        if score[0] == 3:
            cv2.rectangle(frame, (,),(,), )
        if score[1] >= 1:
            cv2.rectangle(frame, (,),(,), )
        if score[1] >= 2:
            cv2.rectangle(frame, (,),(,), )
        if score[1] == 3:
            cv2.rectangle(frame, (,),(,), color , 2, cvline)
    ''' 

    def get_choice_player(self, frame, data):
        if not self.flag_p_choice:
            self.player_choice = self.options[np.argmax(model.predict(data))]
            self.flag_p_choice = True
            
    def get_choice_computer(self):
        if not self.flag_c_choice:
            self.computer_choice = self.options[randint(0,2)]
            self.flag_c_choice = True
    
    def get_winner(self, frame):
        if self.user_Choice == self.computer_Choice:
            cv2.putText(frame, f"You both picked {self.user_Choice}!", (150, 250), font, 1, color, 2, cvline)
            cv2.putText(frame, f"one point each!", (200, 300), font, 1, color, 2, cvline)

            if self.flag_score == False:
                self.score[0]+=1
                self.score[1]+=1          
        elif self.user_Choice == 'Rock' and self.computer_Choice == 'Paper':
            cv2.putText(frame, f"Opponent picked {self.computer_Choice}!", (150, 250), font, 1, color, 2, cvline)
            cv2.putText(frame, f"You Lose... Try Again!", (200, 300), font, 1, color, 2, cvline)
            if self.flag_score == False:
                self.score[1]+=1            
        elif self.user_Choice == 'Paper' and self.computer_Choice == 'Scissors':
            cv2.putText(frame, f"Opponent picked {self.computer_Choice}!", (150, 250), font, 1, color, 2, cvline)
            cv2.putText(frame, f"You Lose... Try Again!", (200, 300), font, 1, color, 2, cvline)
            if self.flag_score == False:
                self.score[1]+=1            
        elif self.user_Choice == 'Scissors' and self.computer_Choice == 'Rock':
            cv2.putText(frame, f"Opponent picked {self.computer_Choice}!", (150, 250), font, 1, color, 2, cvline)
            cv2.putText(frame, f"You Lose... Try Again!", (200, 300), font, 1, color, 2, cvline)        
            if self.flag_score == False:
                self.score[1]+=1            
        else:
            cv2.putText(frame, f"Opponent picked{self.computer_Choice} You Win!", (80, 110), font, 1, color, 2, cvline)
            if self.flag_score == False:
                self.score[0]+=1
        self.flag_score = True

    def final_winner(self, frame):
        if self.score[0] > self.score[1] and self.score[0] > 2:
            print("You Win")
        elif self.score[1] > self.score[0] and self.score[1] > 2:
            print("You Lose")
        else:
            print("draw")

    def playGame(self, frame):
        round_timer = self.round_length * self.game_round
        elapsed_time = time.time()-self.start_time
        if elapsed_time < 3:
            cv2.putText(frame, f"Starting in {int(5 - elapsed_time)}!",(10 , 420), font, 1, color, 2, cvline)
        if elapsed_time > 3 and not self.flag_final:
            self.game_UI(frame)
            cv2.putText(frame, f"Starting in {int(5 - elapsed_time)}!",(10 , 420), font, 1, color, 2, cvline)
            if elapsed_time > (5 + round_timer - 6):
                self.get_choice_player(frame, data)
                cv2.putText(frame, f"{self.player_choice}", (10 , 200), font, 1, color, 2, cvline)
                self.get_choice_computer()
                cv2.putText(frame, f"{self.computer_choice}",(500 , 200), font, 1, color, 2, cvline)
            elif elapsed_time > (5 + round_timer - 3):
                self.get_winner(frame)
            elif elapsed_time > round_timer:
                self.game_round+=1
        if self.score[0] == 5 or self.score[1] == 3:
            self.final_winner(frame)


if __name__ == "__main__":

    game = Game()
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image

        game.playGame(frame)

        cv2.imshow('frame', frame)

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()