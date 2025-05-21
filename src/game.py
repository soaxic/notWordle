from word import *
from constants import GAME_ROUNDS_MAX

class Game():
    def __init__(self, word):
        self._word = word
        self._max_rounds = GAME_ROUNDS_MAX
        self._current_round = 1
        self._current_progress = ["_" for _ in range(self._word.length)]
        self._victory = False
        self.play_again = False
    
    def play(self):
        self._start_game()
        return self.play_again

    def _start_game(self):
        print("Welcome to notWordle!\n")
        while (self._current_round < self._max_rounds) and not (self._victory):
            try:
                self._next_round()
            except ValueError:
                print("\nInvalid input!\n")
        
        if self._current_round == self._max_rounds:
            print("\nMax rounds reached! You lose!")
        
        exiting = False
        while not exiting:
            try:
                self._continue()
                exiting = True
            except ValueError:
                print("\nInvalid input")

    def _next_round(self):
        print(f"Round {self._current_round} of {self._max_rounds}")
        print(" ".join(self._current_progress))
        user_input = str.upper(input("\nEnter your guess: "))
        if len(user_input) != self._word.length:
            raise ValueError
        if user_input == self._word.value:
            self._win_game()
            return
        for i in range(self._word.length):
            if user_input[i] == self._word.value[i]:
                self._current_progress[i] = user_input[i]
        self._current_round += 1

    def _win_game(self):
        print("\n" + " ".join(self._word.value))
        print("\nYOU WIN!")
        self._victory = True

    def _continue(self):
        user_input = str.upper(input("\nPlay again? (Y/N): "))
        match user_input:
            case "Y":
                self.play_again = True
            case "N":
                self.play_again = False
            case _:
                raise ValueError