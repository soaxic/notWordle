import random, csv
from constants import *

class Word():
    def __init__(self, seed=None, debug=False):
        self._debug = debug
        self._seed = seed
        random.seed(self._seed)
        self._point_value = 0
        self.length = 0
        self._get_length()
        self.value = self._get_word(self.length)
        self.valueset = set(self.value)
        if self._debug:
            print(f"DEBUG - Current word: {self.value}")

    def _get_length(self):
        while True:
            try:
                user_input = int(input("\nChoose a difficulty:\n1 - Easy\n2 - Medium\n3 - Hard\n"))
                match user_input:
                    case 1:
                        print("Starting game on Easy!")
                        self._point_value = EASY_POINTS_VALUE
                        self.length = EASY_WORD_LENGTH
                        break
                    case 2:
                        print("Starting game on Medium!")
                        self._point_value = MEDIUM_POINTS_VALUE
                        self.length = MEDIUM_WORD_LENGTH
                        break
                    case 3:
                        print("Starting game on Hard!")
                        self._point_value = HARD_POINTS_VALUE
                        self.length = HARD_WORD_LENGTH
                        break
                    case _:
                        print("\nInvalid input\n\n")
            except ValueError:
                print("\nInvalid input\n\n")
        print("\n\n\n\n\n\n")
        return
            
    def _get_word(self, length):
        match length:
            case 4:
                words_csv = FOUR_LETTER_WORDS_CSV
            case 5:
                words_csv = FIVE_LETTER_WORDS_CSV
            case 6:
                words_csv = SIX_LETTER_WORDS_CSV
        wordlist = []
        with open(words_csv, mode="r", newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for i in csvreader:
                wordlist.append(str.upper(i[0]))
        return wordlist[random.randint(0,len(wordlist))]