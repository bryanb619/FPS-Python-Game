# Main FILE

# Pygame import
import pygame 
# import settings from AppSettings.py
from AppSettings import * 
# import player Settings
from Player import *

from Map import GameWorld

import math

# Window initialization
pygame.init()

ss = pygame.display.set_mode((Width, Height))

# Screen frames
clock = pygame.time.Clock()

# internal variable
Player = PlayerMovement()

# App close system

while True:
    for event in pygame.event.get():
        # if quit is pressed, app will quit
        if event.type == pygame.QUIT:
            # Kill app
            exit()
    # in Player.py get movement function  
    Player.movement()
    #Screen fill color
    ss.fill(Black)
    
    # Player (for the moment!)
    pygame.draw.circle(ss,Green,Player.position,12)
    
    #  Line 
    pygame.draw.line(ss, Green, Player.position,(Player.x + Width * math.cos(Player.angle),Player.y + Width * math.sin(Player.angle)))
    
    #
    pygame.display.flip()
    # Game FPS Standard 60 FPS
    clock.tick(Fps)
    
    
            