#!/usr/bin/env python3

"""
--- VARIABLES AND STRINGS ---
NOTES:
    - Variable names:
        - CASE SENSITIVE
        - Allows underscores '_', but not '-' or '+'.
    - String Quotes
        - fruit = ‘apple’   ←  Single Quotes OR Double Quotes
        - nested = "She said, \"That's a great idea\""  ← escape whichever nested quotes match the main outer quotes (whether they are single or double). Those that don't match the outer quotes do not need to be escaped.
    - String characters are indexed from 0.
        - a = 'apple'
        - e = a[4]  ("e")
    - Functions and Printing:
        - print()
            - fruit = 'apple'
            - print(fruit)
            - print('apple')
        - len  (length)
            - len('apple') => 5
            - len(fruit) => 5  (assuming fruit='apple').
    - Basic OOP:
        - Everything in Python is an object
        - Every object has a type (string, number)
        - "Methods" are "functions" that are run against an object.
            - object.method()
    - String Methods
        - 'Apple': fruit.upper() => "APPLE"   (assuming fruit='apple')
    - String Concatenation
        - print('I ' + 'love ' + 'Python'
        - sentence = first + ' ' + second + '.'
        - * is repetition operator..
            - mystring = 'lance ' * 3
            - e.g. print(myString) => 'lance lance lance '
            - e.g. print('-' * 10) => '----------'
        - Numbers don't automatically cast to a string. (runtime error)
            - print('I love Python ' + str(versionVar) + '.') => 'I love Python 3'
    - Formatting Strings
        - print('I {} Python.'.format('love')) => 'I love Python.'
        - print('{} {} {}'.format('I', 'love', 'Python.') => 'I love Python.'
        - print('I {0} {1}. {1} {0}s me.'.format('love', 'Python')) => 'I love Python. Python loves me.'  <--positional index
        - print('I {} Python.'.format(myVar))
        - format() also converts numbers.
            - print('I love Python {}.'.format(version)) => 'I love Python 3.'
        - Min Column Width
            - print('{0:8} | {1:8}'.format('Fruit', '3')=>
            - 'Fruit   |       3'   (8 chars wide)
            - '<' Left, '^' Center, `>`Right. If missing, Left is assumed.
            - print('{0:>8}'.format('Apple'))=>
            - '   Apple'
        - Formatting number
            - 'f' floating point
            - print('{0:8.2f}'.format(2.33333) => '2.33'
        - User Input:
            - fruit = input() - Accept Standard Input
            - fruit = input('Prompt to display')
    - Summary:
        - Functions: print(), len(), str(), input()
        - String Methods: upper(), lower(), format()

"""

## EXERCISE 1:

animal = 'cat'
vegetable = 'broccoli'
mineral = 'gold'


print('Here is an animal, a vegetable, and a mineral.')
print(animal)
print(vegetable)
print(mineral)
