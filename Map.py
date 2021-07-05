# Map File
from AppSettings import *

text_map = [
    'WWWWWWWWWWWW', 
    'W..........W',
    'W..........W',
    'W..........W',
    'W..........W',
    'W..........W',
    'W..........W',
    'WWWWWWWWWWWW'
]


GameWorld = set()
for y, row in enumerate(text_map):
    # Coordinates enumerate, ( Y COORDINATES)
    for i, char in enumerate(row):
        if char == "W":
            GameWorld.add((i * Tile, y * Tile ))