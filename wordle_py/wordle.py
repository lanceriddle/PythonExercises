#!/usr/bin/env python3

"""
    ** WORDLE PUZZLE SOLVER **
    -- Author: Lance Riddle --

New York Times Wordle:
    - https://www.nytimes.com/games/wordle/index.html

EXAMPLE "TRAINING":
green_letters = [ # List of Tuples
    ("a",4), ("b",5)
]
yellow_letters = [ # List of Tuples
    ("s",1), ("p",5)
]
gray_letters = [ # List of chars
    "q", "u", "e", "r", "y"
]


TODO: Fix bug when duplicate letter is included in 'x' list.
TODO: Only load file once per game, not every time user enters an attempt.
TODO: Keep track of narrowed-down list instead of running through all words with every attempt.
        - And then don't need to keep track of previous restrictions.
        - This can help fix the bug of duplicate letters.
"""

import csv        # For reading the CSV dictionary input.
import itertools  # For looping over multiple lists.
import os         # For accessing the current path of this script, to load dictionary files.
import traceback  # For printing exceptions.
from colors import console_color  # For importing the class of console color definitions.

# GLOBAL VARS:

# The list of words pulled from the wordle JavaScript code:
DICT_FILE = os.path.join(os.path.dirname(__file__), 'dicts/words_from_wordle_site_2022-08-04_list.csv')

MAX_DISPLAY_COLUMNS = 7
column_count = 0
best_word = ''

# LEARNING:
# Letters in the word and in the correct spot (Green Boxes):
green_letters = [ ] # List of Tuples

# Letters in the word but in the wrong spot (Yellow Boxes):
yellow_letters = [ ] # List of Tuples

# Letters not in the word in any spot (Gray Boxes):
gray_letters = [ ] # List of Tuples


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
    """ NOTE: Hacking: Change this to just check that the word doesn't contain the letter
        at the given position. This is sub-optimal since we aren't considering the letter should NOT
        be in the word, but this is a workaround for when the gray letter is a duplicate of a green letter.
        This makes duplicate letters less dangerous (not disqualifying valid words),
        but makes the recommended words less optimal (words we should have disqualified). """
    for letter, position in list:
        #if item in word.lower():
        if (letter == word[position-1].lower()):
            return False
    return True


def check_word(word, count = -1):
    """ For each word, run it through the restrictions and if it passes, print it to the screen. """
    global column_count # Needed to modify global var
    if (len(word) == 5
            and check_green_letters(word, green_letters)
            and check_yellow_letters(word, yellow_letters)
            and check_gray_letters(word, gray_letters)):

        column_count += 1
        # Only include the count if it was provided.
        if (count < 0):
            display_text = "   {}".format(word)
        else:
            display_text = "   {} {:<9}".format(word, "("+str(count)+")")

        if (column_count == MAX_DISPLAY_COLUMNS):
            print(display_text)
            column_count = 0
        else:
            print(display_text, end="")
            #if (int(count) > 100000):
            #    print("   {}{}{} {:<9}".format(console_color.LightGreen, word, console_color.ResetAll, "("+count+")"), end="")
            #else:
            #    print("   {} {:<9}".format(word, "("+count+")"), end="")
        return True # It was a match
    return False # It was not a match.


def find_matches():
    """ Go through a dictionary and find words that match with the learned restrictions. """
    global column_count, best_word # Needed to modify global var
    column_count = 0
    best_word = ''

    try:
        with open(DICT_FILE, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                #print("row[0]: " + str(row[0]) + ";  row[1]: " + str(row[1]))

                result = check_word(row[0])
                if (result == True):
                    best_word = row[0]

        if (best_word != ''):
            print("\n\n Try using: \"" + console_color.LightGreen + best_word + console_color.ResetAll + "\"")

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

        if (color == 'g'):
            green_letters.append(tuple((letter, position)))
        elif (color == 'y'):
            yellow_letters.append(tuple((letter, position)))
        elif (color == 'x'):
            gray_letters.append(tuple((letter, position)))

    #print_memory()


def reset():
    """ Reset the learned letters for a new game. """
    print("\n\n ********************")
    print(" * RESETTING MEMORY *")
    print(" ********************")

    global green_letters, yellow_letters, gray_letters, best_word
    green_letters.clear()
    yellow_letters.clear()
    gray_letters.clear()
    best_word = ''


def print_memory():
    """ Print the current contents of the memory lists. """
    print("\n\n *************")
    print(" *** DEBUG ***")
    print(" *************")

    print(" Green: " + str(green_letters))
    print(" Yellow: " + str(yellow_letters))
    print(" Gray: " + str(gray_letters))


def print_controls():
    """ Print the CLI commands. """
    commands = [ "{}COMMANDS:{}".format(console_color.Underlined, console_color.ResetAll),
                    "r - Reset", "q - Quit", "d - Debug", "<enter> - Use The Suggested Word" ]
    colors = [ ' '*8+"{}COLORS:{}".format(console_color.Underlined, console_color.ResetAll),
                    "g - Green", "y - Yellow", "x - Gray", "- - Ignore" ]

    # Print the list of options in two columns.
    print()
    for (command, color) in itertools.zip_longest(commands, colors, fillvalue=''):
        print("    {:<36}{:<14}".format(command, color))


def main():
    while True:
        print_controls()

        word = input("\n What word did you try? ")
        if (word == 'q'):   # Exit
            exit(0)
        elif (word == 'r'): # Reset the memory for a new game
            reset()
            continue
        elif (word == ''):  # Quickly accept the suggested word
            word = best_word
            print(' '*13 + "You tried: " + word)
        elif (word == 'd'): # Debug
            print_memory()
            continue

        colors = input(" What were the colors?  ")
        if (colors == 'q'):   # Exit
            exit(0)
        elif (colors == 'r'): # Reset the memory for a new game
            reset()
            continue
        elif (colors == 'd'): # Debug
            print_memory()
            continue

        # Update the lists of restrictions.
        learn_from_attempt(word, colors)

        # Print matching words
        print("\n {}Here are some words to try:{}\n".format(console_color.Underlined, console_color.ResetAll))
        find_matches()


# Only run main() when this .py file is executed directly.
if __name__ == '__main__':
    main()
