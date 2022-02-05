#!/usr/bin/env python3

"""
NOTES:
- Functions must be declared above where they are used.
- Arguments can have a default (name = "Lance").
- Arguments can be passed in different orders if labeled.
    def function(arg1, arg2):
    Can be called as function(arg2 = "2", arg1 = "1") and works.
- First line of a function is the "doc string" used by Help feature.
"""

## Exercise 1
story_template = "The {0} {1} {2}."

def get_word(word):
    """Retrieves the words from the user."""
    return input("Please enter a {}: ".format(word))

def fill_in_blanks(adjective, noun, verb):
    """Fills in the blanks in our sentence."""
    return story_template.format(adjective, noun, verb)

def create_story():
    """Creates the story."""
    user_adjective = get_word("adjective")
    user_noun = get_word("noun")
    user_verb = get_word("verb")
    return fill_in_blanks(user_adjective, user_noun, user_verb)
    

print(create_story())

