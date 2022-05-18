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
        self.round_length = 13

    def game_UI(self, frame):
        elapsed_time = int(time.time() - self.start_time)
        cv2.putText(frame, f"Player",  (10, 30), font, 1, color, 2, cvline)
        cv2.putText(frame, f"RPS-BOT", (480, 30), font, 1, color, 2, cvline)
        cv2.putText(frame, f"[{self.score[0]}|{self.score[1]}]", (280, 30), font, 1, color, 2, cvline)
        cv2.putText(frame, f"Round {self.game_round}",(10 , 460), font, 1, color, 2, cvline)
        cv2.putText(frame, f"{elapsed_time}",(10 , 420), font, 1, color, 2, cvline)
        # score ticks
        '''
        if self.score[0] >= 1:
            cv2.rectangle(frame, (,),(,), )
        if self.score[0] >= 2:
            cv2.rectangle(frame, (,),(,), )
        if self.score[0] == 3:
            cv2.rectangle(frame, (,),(,), )
        if self.score[1] >= 1:
            cv2.rectangle(frame, (,),(,), )
        if self.score[1] >= 2:
            cv2.rectangle(frame, (,),(,), )
        if self.score[1] == 3:
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
        if self.player_choice == self.computer_choice:
            cv2.putText(frame, f"You both picked {self.player_choice}!", (150, 250), font, 1, color, 2, cvline)
            cv2.putText(frame, f"one point each!", (200, 300), font, 1, color, 2, cvline)
            if self.flag_score == False:
                self.score[0]+=1
                self.score[1]+=1

        elif self.player_choice == 'Rock' and self.computer_choice == 'Paper':
            cv2.putText(frame, f"Opponent picked {self.computer_choice}!", (150, 250), font, 1, color, 2, cvline)
            cv2.putText(frame, f"You Lose... Try Again!", (200, 300), font, 1, color, 2, cvline)
            if self.flag_score == False:
                self.score[1]+=1

        elif self.player_choice == 'Paper' and self.computer_choice == 'Scissors':
            cv2.putText(frame, f"Opponent picked {self.computer_choice}!", (150, 250), font, 1, color, 2, cvline)
            cv2.putText(frame, f"You Lose... Try Again!", (200, 300), font, 1, color, 2, cvline)
            if self.flag_score == False:
                self.score[1]+=1

        elif self.player_choice == 'Scissors' and self.computer_choice == 'Rock':
            cv2.putText(frame, f"Opponent picked {self.computer_choice}!", (150, 250), font, 1, color, 2, cvline)
            cv2.putText(frame, f"You Lose... Try Again!", (200, 300), font, 1, color, 2, cvline)        
            if self.flag_score == False:
                self.score[1]+=1            
        else:
            cv2.putText(frame, f"Opponent picked{self.computer_choice} You Win!", (80, 110), font, 1, color, 2, cvline)
            if self.flag_score == False:
                self.score[0]+=1
        self.flag_score = True

    def final_winner(self, frame):
        if self.score[0] > self.score[1] and self.score[0] > 2:
            cv2.putText(frame, f"You win {self.score[0]} rounds to {self.score[1]}", (80, 110), font, 1, color,2, cvline)
            self.flag_final = True
        elif self.score[1] > self.score[0] and self.score[1] > 2:
            print("You Lose")
            self.flag_final = True
        else:
            print("draw")
            self.flag_final = True

    '''
    if   score[0] >  score[1]:
        cv2.putText(frame, f"You win {score[0]} rounds to {score[1]}", (80, 110), font, 1, color,2, cvline)
    elif score[0] == score[1]:
        cv2.putText(frame, f"you drew with {self.score[0]} rounds each", (80, 110), font, 1, color, 2, cvline)
    elif score[0] <  score[1]:
        cv2.putText(frame, f"you lost {self.score[1]} rounds to {self.score[0]}", (80, 110), font, 1, color, 2, cvline)
    '''

    def round_reset(self):
        self.flag_c_choice = False
        self.flag_p_choice = False
        self.flag_score = False
        self.flag_final = False

    def playGame(self, frame):
        elapsed_time = time.time()-self.start_time
        if elapsed_time < 5:
            cv2.putText(frame, f"Starting in {int(5 - elapsed_time)}!",(10 , 420), font, 1, color, 2, cvline)
        if elapsed_time > 5 and not self.flag_final:
            self.game_UI(frame)
            if elapsed_time > 5 and (4 - (elapsed_time-5)) > 0:
                cv2.putText(frame, f"{int(4 - (elapsed_time-5))}!",(250 , 250), font, 3, color, 2, cvline)
            
            if elapsed_time > (5 + self.round_length - 10):
                self.get_choice_player(frame, data)
                cv2.putText(frame, f"{self.player_choice}", (10 , 200), font, 1, color, 2, cvline)
                self.get_choice_computer()
                cv2.putText(frame, f"{self.computer_choice}",(500 , 200), font, 1, color, 2, cvline)
            if elapsed_time > (5 + self.round_length - 5):
                self.get_winner(frame)
                cv2.putText(frame, "Winner",(200 , 200), font, 3, color, 2, cvline)
            if elapsed_time > 5 + self.round_length:
                self.start_time = time.time() - 5
                self.round_reset()
                self.game_round += 1
                
        
        if self.score[0] == 3 or self.score[1] == 3:
            elapsed_time = time.time() - self.start_time()
            if elapsed_time < 5:
                print(self.start_time)
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