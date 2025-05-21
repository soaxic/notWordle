import sys
from word import *
from game import *
from saves import *

def main(args):
    print("Welcome to notWordle!\n")
    welcome()
    total_points = 0
    debug = False
    for i in range(len(args)):
        if args[i] == "-Debug":
            debug = True
            args[i] = None
    try:
        seed = args[1]
    except IndexError:
        seed = None
    if debug:
        print("\n=====DEBUG MODE ON=====")
    try:
        loop = True
        while loop:
            word = Word(seed=seed, debug=debug)
            game = Game(word)
            loop,points = game.play()
            total_points += points
            print(f"\nYour score is: {total_points}\n")
        if debug:
            print("\n=====DEBUG MODE ON=====")
        print("\n\nThanks for playing!")
    except KeyboardInterrupt:
        print("\n\nThanks for playing!")

main(sys.argv)