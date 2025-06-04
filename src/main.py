import config
from saves import *
from word import *
from game import *
from cli_parser import parse_cli_arguments
from constants import CLEAR_SCREEN

def main():
    print(CLEAR_SCREEN)
    print("Welcome to notWordle!\n")
    args = parse_cli_arguments()
    config.DEBUG_MODE = args.debug
    config.SEED = args.seed
    save = Save()
    try:
        session_points = 0
        loop = True
        while loop:
            word = Word()
            game = Game(word)
            loop,points = game.play()
            session_points += points
            print(CLEAR_SCREEN)
            print(f"Your score is: {session_points}\n")
        if config.DEBUG_MODE:
            print("\n=====DEBUG MODE ON=====")
        save.save_and_quit(session_points)
        print("\n\nThanks for playing!")
    except KeyboardInterrupt:
        save.save_and_quit(session_points)
        print("\n\nThanks for playing!")

main()