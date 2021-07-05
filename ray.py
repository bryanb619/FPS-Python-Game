# Ray Settings File

# imports
import pygame
from AppSettings import *
# Game Map
from Map import GameWorld

# Ray function
def RayCasting(ss, PlayerPosition, PlayerAngle):
    
    currentAngle = PlayerAngle - HalfView
    # Inicial positions Xo & Yo
    xo, yo = playerPosition
    # Display of Ray cast
    for ray in range(rays):
        # Math for Rays
        sin_m = math.sin(currentAngle)
        cos_m = math.cos(currentAngle)
        # Depth view
        for depth in range(FullDepth):
            
            x = xo + depth * cos_m
            y = yo + depth * sin_m
            #
            pygame.draw.line(ss, Gray, playerPosition, (x,y), 2)
            
            if (x // Tile * Tile, y // Tile * Tile) in GameWorld:
                projHeight = projC / depth
                # Walls drawing
                pygame.draw.rect(ss, Gray, (ray * Scale, HalfHeight - projHeight // 2, Scale, projHeight))
                # Break if
                break
        # 
        currentAngle += deltaAngle 