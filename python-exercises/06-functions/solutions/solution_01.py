#!/usr/bin/env python3

def get_word(word_type):
    """Get a word from a user and return that word."""

    # The lower() function converts the string to lowercase before testing it
    if word_type.lower() == 'adjective':
        # Use 'an' in front of 'adjective'
        a_or_an = 'an'
    else:
        # Otherwise, use 'a' in front of 'noun' or 'verb'
        a_or_an = 'a'
    return input('Enter a word that is {0} {1}: '.format(a_or_an, word_type))


def fill_in_the_blanks(noun, verb, adjective):
    """Fills in the blanks and returns a completed story."""

    # The \ lets the string continue on the next line to make the code easier to read
    story = "In this course you will learn how to {1}.  " \
            "It's so easy even a {0} can do it.  " \
            "Trust me, it will be very {2}.".format(noun, verb, adjective)
    return story


def display_story(story):
    """Displays a story."""
    print()
    print('Here is the story you created.  Enjoy!')
    print()
    print(story)


def create_story():
    """Creates a story by capturing the input and displaying a finished story."""
    noun = get_word('noun')
    verb = get_word('verb')
    adjective = get_word('adjective')

    the_story = fill_in_the_blanks(noun, verb, adjective)
    display_story(the_story)

create_story()
