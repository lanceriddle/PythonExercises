#!/usr/bin/env python3

"""
NOTES:
    - Tuples are immutable, ordered, indexed lists.
        tuple = ("Monday", "Tuesday")
    - If you want a single item, it must be followed by ',' (item_1,)
    - Used if you don't want the list altered.
    - Conversion functions: list(x), tuple(x), type(x)
    
    - Pulling out items:
        weekend = ("Saturday", "Sunday")
        (sat, sun) = weekend
        print(sat) <--- Prints "Saturday"
    
    - You can return a tuple from a function.
        return (highest, lowest)
        (highest, lowest) = function()
    
    - max(tuple), min(tuple) returns max/min values respectively.

"""

## Exercise 1

airports = [
    ("O'Hare Intl. Airport", "ORD"),
    ("Los Angeles Intl. Airport", "LAX"),
    ("Dallas/Fort Worth Intl. Airport", "DFW"),
    ("Denver Intl. Airport", "DEN")
]

for (airport, code) in airports:
    print("The code for {} is {}.".format(airport, code))

