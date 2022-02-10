#!/usr/bin/env python3

"""
--- DICTIONARIES ---
NOTES:
    - Delete:
        del <dict>[<item>]
    - if "<key>" in <dict>.keys():
    - if "<value>" in <dict>.values():
    - for contact in contacts:
        # dictionary_name[key_variable]
        # no guarantee of order.
    - for key_variable, value_variable in dictionary_name.items():
    - You can nest dictionaries (JSON-style syntax).
        print(contacts["Jason"]["phone"])

"""

## Exercise 1

def print_facts(facts):
    """Display rows of the dictionary."""
    print()
    for person, fact in facts.items():
        print("{0}: {1}".format(person, fact))
    
    # Alternatively
    #for fact in facts:
    #    print("{}: {}".format(fact, facts[fact]))


# Initialize a dictionary and print it.
people_facts = {
    "Alice": "Is from New York.",
    "Bob": "Is from California."
}

print_facts(people_facts)


# Modify the dictionary and print it again.
people_facts["Alice"] = "Moved to Florida."
people_facts["Charlie"] = "Is from Texas."

print_facts(people_facts)
