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
"""

import os
import traceback

"""
EXAMPLES:
matching_list = { # List of Tuples
    ("r",4),
    ("y",5)
}
contain_but_not_match_list = { # List of Tuples
    ("s",1),
    ("s",5)
}
word_not_contains_list = [ # List of chars
    "q", "u", "e", "r", "y"
]
"""

matching_list = { # List of Tuples  # TODO: Read these from an XLS??
    ("r",2),
    ("r",5)
}
contain_but_not_match_list = { # List of Tuples
    ("e",3),
    ("r",4),
    ("e",5),
    ("o",1),
    ("e",4)
}
word_not_contains_list = [ # List of chars
    "q", "u", "y", "p", "i", "c", "d"
]


def word_matches_list(word, list):
    for letter, position in list:
        if not (letter == word[position-1].lower()):
            return False
    return True

def word_contain_but_not_match_list(word, list):
    for letter, position in list:
        if (letter == word[position-1].lower()
                or not letter in word.lower()):
            return False
    return True

def word_not_contains(word, list):
    for item in list:
        if item in word.lower():
            return False
    return True

max_columns = 5
column_count = 0
def check_word(word):
    global column_count # Needed to modify global var
    if (len(word) == 5):
        if (word_matches_list(word, matching_list)
                and word_contain_but_not_match_list(word, contain_but_not_match_list)
                and word_not_contains(word, word_not_contains_list)
                ):
            if (column_count > max_columns):
                print(word)
                column_count = 0
            else:
                print(word + "     ", end = "")
                column_count += 1

input_path = os.path.join(os.path.dirname(__file__), 'usa.txt')

def main():
    try:
        with open(input_path, 'r') as file:
            for word in file:
                check_word(word.rstrip())
    except Exception as e:
        print("Error processing file: " + str(e))
        traceback.print_exc()


# Only run main() when this .py file is executed directly.
if __name__ == '__main__':
    main()
