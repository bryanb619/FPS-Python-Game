# Map File
from AppSettings import *

text_map = [
    'WWWWWWWWWWWW',
    'W......W...W',
    'W..WWW...W.W',
    'W....W..WW.W',
    'W..W....W..W',
    'W..W...WWW.W',
    'W....W.....W',
    'WWWWWWWWWWWW'
]   


GameWorld = set()
for j, row in enumerate(text_map):
    # Coordinates enumerate, ( Y COORDINATES)
    for i, char in enumerate(row):
        if char == "W":
            GameWorld.add((i * Tile, j * Tile ))