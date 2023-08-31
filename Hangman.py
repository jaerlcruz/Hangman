import random
"""
     +---+
     O/  |
    /|   |  Welcome to Jae's Hangman game!
    / \  |
    =======
    This is a quick little project for me to practice making a Python program
    on my own, without directions.

"""
class Hangman():
    def __init__(self):
        self.correct = ''
        self.wrong = ''
        self.word = ''
        
    
    #Get word from word list. Pull from Wordle/Scrabble/etc...
    def word_choice(self):
        pass

    # Get letter input. Input must be a new letter.
    def get_letter(self, letter):
        pass

    # Show spaces, display correct/incorrect letters.
    def display_text(self):
        pass

    # Print Hangman status; 6 body parts total. Show remaining wrong guesses
    def display_person(self):
        pass
