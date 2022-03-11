#!/usr/bin/env python3

"""
    ** WORDLE PUZZLE SOLVER **
    -- Author: Lance Riddle --

New York Times Wordle:
    - https://www.nytimes.com/games/wordle/index.html
Wordle Archive:
    - https://www.devangthakkar.com/wordle_archive/
Dictionary files source:
    - http://www.gwicks.net/dictionaries.htm

EXAMPLE "TRAINING":
green_letters = { # List of Tuples
    ("r",4),
    ("y",5)
}
yellow_letters = { # List of Tuples
    ("s",1),
    ("s",5)
}
gray_letters = [ # List of chars
    "q", "u", "e", "r", "y"
]
"""

"""
TODO: Fix bug when duplicate letter is included in 'x' list.
TODO: Display user instructions (x, y, g, etc).
TODO: Implement 'r' reset command.
TODO: Suggest word based on most common. (If new dictionary, filter down to 5-letter words)
TODO: Only load file once per game, not every time user enters an attempt.
TODO: Keep track of narrowed-down list instead of running through all words with each entered attempt.
"""

import os
import traceback

# Global Vars:
DICT_FILE = os.path.join(os.path.dirname(__file__), 'usa_5-letters.txt')
MAX_DISPLAY_COLUMNS = 8
column_count = 0

# Learning:
# Letters in the word and in the correct spot (Green Boxes):
green_letters = [ ] # List of Tuples

# Letters in the word but in the wrong spot (Yellow Boxes):
yellow_letters = [ ] # List of Tuples

# Letters not in the word in any spot (Gray Boxes):
gray_letters = [ ] # List of chars


def check_green_letters(word, list):
    """ Make sure the word contains the letters at the given positions (Green Boxes). """
    for letter, position in list:
        if not (letter == word[position-1].lower()):
            return False
    return True

def check_yellow_letters(word, list):
    """ Make sure the word contains the letters, but NOT at the given positions (Yellow Boxes). """
    for letter, position in list:
        if (letter == word[position-1].lower()
                or not letter in word.lower()):
            return False
    return True

def check_gray_letters(word, list):
    """ Make sure the word does NOT contain any of the letters, in any position (Gray Boxes). """
    for item in list:
        if item in word.lower():
            return False
    return True


def check_word(word):
    """ For each word, run it through the restrictions and if it passes, print it to the screen. """
    global column_count # Needed to modify global var
    if (len(word) == 5
            and check_green_letters(word, green_letters)
            and check_yellow_letters(word, yellow_letters)
            and check_gray_letters(word, gray_letters)):
        column_count += 1
        if (column_count == MAX_DISPLAY_COLUMNS):
            print("     " + word)
            column_count = 0
        else:
            print("     " + word, end="")


def old_main():
    global column_count # Needed to modify global var
    try:
        with open(DICT_FILE, 'r') as file:
            for word in file:
                check_word(word.rstrip())
            column_count = 0
    except Exception as e:
        print("Error processing file: " + str(e))
        traceback.print_exc()


""" ** WORDLE V2 ** """

def learn_from_attempt(word, colors):
    """ Learning from the results of the attempt. """
    global green_letters, yellow_letters, gray_letters
    print("\n Learning from your failure...")
    
    letters = list(word.lower())
    color_codes = list(colors.lower())
    
    position = 0
    for (letter, color) in zip(letters, color_codes):
        position += 1
        #print(" letter: " + letter + ";  color: " + color + ";  position: " + str(position))
        
        if (color == 'g'):
            green_letters.append(tuple((letter, position)))
        elif (color == 'y'):
            yellow_letters.append(tuple((letter, position)))
        elif (color == 'x'):
            gray_letters.append(letter)
            
    #print(" Green: " + str(green_letters))
    #print(" Yellow: " + str(yellow_letters))
    #print(" Gray: " + str(gray_letters))


def main():
    while True:
        word = input("\n\n What word did you try? ")
        if (word == 'q'):
            exit(0)
            
        colors = input("\n What were the colors?  ")
        if (colors == 'q'):
            exit(0)
        
        # Update the lists of restrictions.
        learn_from_attempt(word, colors)
                
        # Print matching words
        print("\n Here are some words to try:\n")
        old_main()


# Only run main() when this .py file is executed directly.
if __name__ == '__main__':
    main()
