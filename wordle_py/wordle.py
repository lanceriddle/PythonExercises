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
Dictionary with Frequencies:
    - https://en.lexipedia.org/

EXAMPLE "TRAINING":
green_letters = [ # List of Tuples
    ("r",4),
    ("y",5)
]
yellow_letters = [ # List of Tuples
    ("s",1),
    ("s",5)
]
gray_letters = [ # List of chars
    "q", "u", "e", "r", "y"
]


TODO: Fix bug when duplicate letter is included in 'x' list.
TODO: Only load file once per game, not every time user enters an attempt.
TODO: Keep track of narrowed-down list instead of running through all words with every attempt.
TODO: Print word on a gradient of color depending on frequency (0 - 1M).
"""

import csv
import os
import traceback
from colors import colors

# Global Vars:
#DICT_FILE = os.path.join(os.path.dirname(__file__), 'dicts/usa_5-letters_freq_sorted-alpha.csv')
DICT_FILE = os.path.join(os.path.dirname(__file__), 'dicts/usa_5-letters_freq_sorted-frequency.csv')
MAX_DISPLAY_COLUMNS = 7
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


def check_word(word, count=0):
    """ For each word, run it through the restrictions and if it passes, print it to the screen. """
    global column_count # Needed to modify global var
    if (len(word) == 5
            and check_green_letters(word, green_letters)
            and check_yellow_letters(word, yellow_letters)
            and check_gray_letters(word, gray_letters)):
        column_count += 1
        if (column_count == MAX_DISPLAY_COLUMNS):
            #print("     " + word)
            print("   {} {:<9}".format(word, "("+count+")"))
            column_count = 0
        else:
            #print("     " + word, end="")
            print("   {} {:<9}".format(word, "("+count+")"), end="")
        return True # It was a match
    return False # It was not a match.


def old_main():
    global column_count # Needed to modify global var
    column_count = 0
    best_word = ''
    best_count = -1
    
    try:
        with open(DICT_FILE, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                #print("row[0]: " + str(row[0]) + ";  row[1]: " + str(row[1]))
                result = check_word(row[0], row[1])
                if (result == True and int(row[1]) > int(best_count)):
                    best_word = row[0]
                    best_count = row[1]
        if (best_word != ''):
            print("\n\n I recommend trying: \"" + colors.LightGreen + best_word + colors.ResetAll + "\"")
            
    except Exception as e:
        print("Error processing file: " + str(e))
        traceback.print_exc()


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


def reset():
    """ Reset the learned letters for a new game. """
    print("\n RESETTING MEMORY...")
    global green_letters, yellow_letters, gray_letters
    green_letters = yellow_letters = gray_letters = []


def main():
    while True:
        print("\n\n CONTROLS:")
        print(" Green ('g'), Yellow ('y'), Gray ('x'), Ignore ('-')")
        print(" Reset ('r'), Quit ('q')")
        word = input("\n What word did you try? ")
        if (word == 'q'):
            exit(0)
        elif (word == 'r'):
            reset()
            continue
            
        colors = input("\n What were the colors?  ")
        if (colors == 'q'):
            exit(0)
        elif (word == 'r'):
            reset()
            continue
        
        # Update the lists of restrictions.
        learn_from_attempt(word, colors)
                
        # Print matching words
        print("\n Here are some words to try:\n")
        old_main()


# Only run main() when this .py file is executed directly.
if __name__ == '__main__':
    main()
