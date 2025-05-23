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
        return self.play_again, self._word._point_value

    def _start_game(self):
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
        self._check_letters(user_input)
        self._current_round += 1

    def _win_game(self):
        print("\n" + " ".join(self._word.value))
        print("\nYOU WIN!")
        self._victory = True

    def _check_letters(self, user_input):
        check = {}
        for i in range(self._word.length):
            check[i] = {"value":user_input[i],"in_word":False, "in_spot":False}
            if user_input[i] in self._word.valueset:
                check[i]["in_word"] = True
            if user_input[i] == self._word.value[i]:
                self._current_progress[i] = user_input[i]
                check[i]["in_spot"] = True
        
        for i in range(self._word.length):
            if check[i]["in_word"]:
                if check[i]["in_spot"]:
                    print(f"{check[i]["value"]} - Correct Letter, Correct Spot")
                else:
                    print(f"{check[i]["value"]} - Correct Letter, Incorrect Spot")
            else:
                print(f"{check[i]["value"]} - Incorrect Letter, Incorrect Spot")


    def _continue(self):
        user_input = str.upper(input("\nPlay again? (Y/N): "))
        match user_input:
            case "Y":
                self.play_again = True
            case "N":
                self.play_again = False
            case _:
                raise ValueError