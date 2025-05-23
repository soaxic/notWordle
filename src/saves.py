import os
from constants import SAVES_FOLDER

def welcome():
    if not os.path.exists(SAVES_FOLDER):
        os.mkdir(SAVES_FOLDER)
    username = input("What is your name? ")
    usersave = SAVES_FOLDER + "/" + str.lower(username) + ".txt"
    if not os.path.exists(usersave):
        with open(usersave, 'w') as f:
            f.write(f"player_name:{username}\n")
        print(f"Thanks for trying notWordle, {username}!\n")
        return
    print(f"\nWelcome back {username}!\n")
    return