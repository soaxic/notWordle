import config
from word import *
from game import *
from saves import *
from cli_parser import parse_cli_arguments

def main():
    print("Welcome to notWordle!\n")
    args = parse_cli_arguments()
    config.DEBUG_MODE = args.debug
    config.SEED = args.seed
    welcome()
    try:
        loop = True
        while loop:
            word = Word()
            game = Game(word)
            loop,points = game.play()
            total_points += points
            print(f"\nYour score is: {total_points}\n")
        if config.DEBUG_MODE:
            print("\n=====DEBUG MODE ON=====")
        print("\n\nThanks for playing!")
    except KeyboardInterrupt:
        print("\n\nThanks for playing!")

main()