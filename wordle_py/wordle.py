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

import os
import traceback

# Global Vars:
DICT_FILE = os.path.join(os.path.dirname(__file__), 'usa.txt')
MAX_DISPLAY_COLUMNS = 5
column_count = 0

# WORD RESTRICTIONS:
# In the word and correct spot (Green Boxes):
green_letters = { # List of Tuples
    ("r",2)
}
# In the word but wrong spot (Yellow Boxes):
yellow_letters = { # List of Tuples
    ("e",3),
    ("r",4)
}
# Not in the word in any spot (Gray Boxes):
gray_letters = [ # List of chars
    "q", "u"
]


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
            print(word)
            column_count = 0
        else:
            print(word + "     ", end="")


def main():
    try:
        with open(DICT_FILE, 'r') as file:
            for word in file:
                check_word(word.rstrip())
    except Exception as e:
        print("Error processing file: " + str(e))
        traceback.print_exc()


# Only run main() when this .py file is executed directly.
if __name__ == '__main__':
    main()
