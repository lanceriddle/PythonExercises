#!/usr/bin/env python3

"""
--- MODULES ---
NOTES:
    - import <module_name>
    - from <module_name> import <method_name1>, <method_name2>  # Now use <method_name1>()
    - >>> dir(<module>)    #(prints the contents of the module)
    - sys.path.append("/Users/user/python") # Add an additional path for looking for modules
    - PYTHONPATH environment variable of paths.
    - Python Standard Library: https://docs.python.org/3/library/
    - if __name__ == '__main__':   # Will be true if this .py file was executed, false if this .py was only imported.

"""

## EXERCISE 1 PART 1
## *****************

def draw_cat(message):
    """Draw a cat saying the appropriate message."""
    messageLen = len(message)
    print('            {}'.format('_' * messageLen))
    print('          < {} >'.format(message))
    print('            {}'.format('-' * messageLen))
    print('          /')
    print(' /\_/\   /')
    print('( o.o )')
    print(' > ^ <')

def main():
    # Get the input from the user.
    message = input('What would you like the cat to say? ')
    draw_cat(message)

# Only run main() when this .py file is executed directly.
if __name__ == '__main__':
    main()

