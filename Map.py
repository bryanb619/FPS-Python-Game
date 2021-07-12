# Map File
from AppSettings import *

""" Game Map"""

# Text map
text_map = [

    'IIIIIIIIIIII',  #  Row 1
    'II...III...I',  #  Row 2
    'I..III...I.I',  #  Row 3
    'I....I..I..I',  #  Row 4
    'I..I..I....I',  #  Row 5
    'I..II...II.I',  #  Row 6
    'I.....I....I',  #  Row 7
    'IIIIIIIIIIII'   #  Row 8
]

"""Transformation of text map in rays """

#Text Map in Walls for every I
GameMap = set()

for b, row in enumerate(text_map):
    for a, char in enumerate(row):
        if char == 'I':
            GameMap.add((a * walls, b * walls))
        
            

# Other cubes (TO BE ADDED)
