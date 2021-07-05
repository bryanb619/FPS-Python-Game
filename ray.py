# Ray Settings File

# imports
import pygame
from AppSettings import *
from Map import GameWorld

# Ray function
def RayCasting(ss, PlayerPosition, PlayerAngle):
    
    currentAngle = PlayerAngle - HalfView
    xo, yo = playerPosition
    
    for ray in range(rays):
        
        sin_m = math.sin(currentAngle)
        cos_m = math.cos(currentAngle)
        
        for depth in range(FullDepth):
            
            x = xo + depth * cos_m
            y = yo + depth * sin_m
            
            pygame.draw.line(ss, Gray, playerPosition, (x,y), 2)
            
            if (x // Tile * Tile, y // Tile * Tile) in GameWorld:
                break
        #
        currentAngle += deltaAngle 