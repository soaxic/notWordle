import sys
from word import *
from game import *

def main(args):
    loop = True
    while loop:
        word = Word(args)
        game = Game(word)
        loop = game.play()
    print("\nThanks for playing!")

main(sys.argv)