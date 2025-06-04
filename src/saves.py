import os
from constants import SAVES_FOLDER, CLEAR_SCREEN

class Save():
    def __init__(self):
        self.welcome()

    def welcome(self):
        if not os.path.exists(SAVES_FOLDER):
            os.mkdir(SAVES_FOLDER)
        self.username = input("What is your name? ")
        self.usersave = SAVES_FOLDER + "/" + str.lower(self.username) + ".txt"
        if not os.path.exists(self.usersave):
            with open(self.usersave, 'w') as f:
                f.write(f"player_name:{self.username}\n")
                f.write("lifetime_score:0")
            self.lifetime_score = 0
            print(CLEAR_SCREEN)
            print(f"Thanks for trying notWordle, {self.username}!\n")
            return
        else:
            with open(self.usersave, 'r') as f:
                for line in f:
                    if line.startswith("lifetime_score:"):
                        self.lifetime_score = int(line.lstrip("lifetime_score:"))
            print(CLEAR_SCREEN)
            print(f"Welcome back {self.username}!\n")
        return
    
    def save_and_quit(self, session_points):
        self.lifetime_score += session_points
        with open(self.usersave, 'w') as f:
            f.write(f"player_name:{self.username}\n")
            f.write(f"lifetime_score:{self.lifetime_score}")
        print(f"Your lifetime point total is: {self.lifetime_score}")
        return