import random, csv

class Word():
    def __init__(self, args):
        try:
            self._seed = args[1]
            random.seed(self._seed)
        except IndexError:
            self._seed = None
            random.seed()
        self._length = self.get_length()
        self.word = self.get_word(self._length)
        print(self.word)

    def get_length(self):
        length = 0
        while length == 0:
            try:
                user_input = int(input("Choose a difficulty:\n1 - Easy\n2 - Medium\n3 - Hard\n"))
                match user_input:
                    case 1:
                        print("Starting game on Easy!")
                        length = 4
                    case 2:
                        print("Starting game on Medium!")
                        length = 5
                    case 3:
                        print("\nNYI - Please try again\n\n")
                    case _:
                        print("\nInvalid input\n\n")
            except ValueError:
                print("\nInvalid input\n\n")
        return length
            
    def get_word(self, length):
        match length:
            case 4:
                words_csv = "content/four_letter_words.csv"
            case 5:
                words_csv = "content/five_letter_words.csv"
            case 6:
                words_csv = "content/six_letter_words.csv"
        wordlist = []
        with open(words_csv, mode="r", newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for i in csvreader:
                wordlist.append(str.upper(i[0]))
        return wordlist[random.randint(0,len(wordlist))]