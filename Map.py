# Map File
from AppSettings import *

"""Criação do Mapa em Text Map"""

text_map = [
    'IIIIIIIIIIII',
    'I......I...I',
    'I..III...I.I',
    'I....I..I..I',
    'I..I....I..I',
    'I..I...III.I',
    'I..........I',
    'IIIIIIIIIIII'
]


"""Transform Text Map in Walls for every "I"""

GameMap = set()

for b, row in enumerate(text_map):
    for a, char in enumerate(row):
        if char == 'I':
            GameMap.add((a * walls, b * walls))
            

# Other cubes (TO BE ADDED)
