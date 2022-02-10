#!/usr/bin/env python3

"""
--- BOOLEANS AND CONDITIONALS ---
"""

## Exercise 1:

# Thresholds in miles:
max_walking = 3
max_driving = 300

# Get user's input and convert to a number:
miles_str = input("How far would you like to travel in miles? ")
miles = float(miles_str)

# Give advice:
if miles < max_walking:
    print("You should walk.")
elif miles < max_driving:
    print("You should drive.")
else:
    print("You should fly.")


# Alternately:
if miles < max_walking:
    verb = "walk"
elif miles < max_driving:
    verb = "drive"
else:
    verb = "fly"

print("You should {}.".format(verb))
