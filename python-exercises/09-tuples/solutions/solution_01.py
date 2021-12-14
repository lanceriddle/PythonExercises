#!/usr/bin/env python3

airports = [
    ("O’Hare International Airport", 'ORD'),
    ('Los Angeles International Airport', 'LAX'),
    ('Dallas/Fort Worth International Airport', 'DFW'),
    ('Denver International Airport', 'DEN')
]

for (airport, code) in airports:
    print('The code for {} is {}.'.format(airport, code))
