import random
with open(r"C:\Users\justi\OneDrive - CSULB\Documents\GitHub\Hangman\HangmanWords.txt") as f: # r before the file path to specify that it's raw string
    words = f.read().split('\n')
"""
     +---+
     O/  |
    /|   |  Welcome to Jae's Hangman game!
    / \  |
    =======
    This is a quick little project for me to practice making a Python program on my own.
    This version of Hangman:
        - does not allow the user to guess the entire word.
        - does not support phrases (single words only, lower case).

"""
class Hangman():
    def __init__(self):
        self.correct = []
        self.wrong = []
        self.word = random.choice(words)
        self.reveal = ['_']*len(self.word)
        # What else?

    
    # Get letter input. Input must be a new letter.
    def get_letter(self):
        valid = False
        letter = None
        while not valid:
            letter = input('Guess a letter: ').lower()
            if letter.isalpha() and letter not in self.correct and letter not in self.wrong:
                valid = True
            else:
                print("Invalid input - must be a new letter")
        if letter in self.word:
            self.correct.append(letter)
        else:
            self.wrong.append(letter)


    # Show spaces, display correct/incorrect letters.
    def reveal_text(self):
        wrong_letters = ''
        for i in range(len(self.word)):
            if self.word[i] in self.correct:
                self.reveal[i] = self.word[i]
            '''elif i in self.wrong:
                wrong_letters += i + ' '''
        print(f"\n{''.join(self.reveal)}\n\nWrong letters guessed: {', '.join(self.wrong)}")
                

    # Print Hangman status; 6 body parts total. Show remaining wrong guesses
    def display_person(self):
        if len(self.wrong) < 1:
            print('''\n +---+\n     |\n     |\n     |\n=======''')
        elif len(self.wrong) == 1:
            print('''\n +---+\n O   |\n     |\n     |\n=======''' + "\n5 incorrect guesses left.")
        elif len(self.wrong) == 2:
            print('''\n +---+\n O   |\n/    |\n     |\n=======''' + "\n4 incorrect guesses left.")
        elif len(self.wrong) == 3:
            print('''\n +---+\n O   |\n/|   |\n     |\n=======''' + "\n3 incorrect guesses left.")
        elif len(self.wrong) == 4:
            print('''\n +---+\n O   |\n/|\  |\n     |\n=======''' + "\n2 incorrect guesses left.")
        elif len(self.wrong) == 5:
            print('''\n +---+\n O   |\n/|\  |\n/    |\n=======''' + "\n1 incorrect guess left.")
        elif len(self.wrong) == 6:
            print('''\n +---+\n O   |\n/|\  |\n/ \  |\n=======''' + "\nGame Over!")


def main():
    h = Hangman()
    print("---- Hangman start! ----\n Guess the word to win!")
    h.display_person()
    while len(h.wrong) != 6:
        h.get_letter()
        h.reveal_text()
        h.display_person()
        if '_' not in h.reveal:
            break
    print("Game over!")

# Implement quit.

if __name__ == "__main__":
    main()