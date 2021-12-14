#!/usr/bin/env python3


def cat_say(text):
    """Generate a picture of a cat saying something"""
    text_length = len(text)
    print('            {}'.format('_' * text_length))
    print('          < {} >'.format(text))
    print('            {}'.format('-' * text_length))
    print('          /')
    print(' /\_/\   /')
    print('( o.o )')
    print(' > ^ <')


def main():
    text = input('What would you like the cat to say? ')
    cat_say(text)

if __name__ == '__main__':
    main()
