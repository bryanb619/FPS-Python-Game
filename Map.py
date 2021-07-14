"""# Map File"""
from AppSettings import *

""" Game Map"""

# Text map array

# I == Wall
# other char == empty space
text_map = [

    'IIIIIIIIIIII',  # Row 1
    'II..II....I',  # Row 2
    'I..II....I.I',  # Row 3
    'I....I..I..I',  # Row 4
    'I..I..I....I',  # Row 5
    'I..II....I.I',  # Row 6
    'I..I..I....I',  # Row 7
    'II......I.I',  # Row 8
    'III.....I..I',  # Row 9
    'II..I....I.I',  # Row 10
    'IIIIIIIIIIII'  # Row 12
]

"""Transformation of text map in rays """

# Text Map in Walls for every I
GameMap = set()

for b, row in enumerate(text_map):
    for a, char in enumerate(row):
        # if char == I, add wall ray
        if char == 'I':
            # Add wall
            GameMap.add((a * walls, b * walls))

# Other cubes (TO BE ADDED)
