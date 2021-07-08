"""Main FILE"""

# Python Modules
import pygame, math

# File import
# Game Main Settings file
from AppSettings import *

# import player Settings from PlayerScript
from PlayerScript import Player

# Import Game Map
from Map import GameMap

# Import Ray Casting from Ray.py
from Ray import ray_casting


"""Window initialization"""
pygame.init()


""" Screen Configuration """
 
# Width = X(800), Height = Y(600)
Screen = pygame.display.set_mode((x, y))
# Screen frames
clock = pygame.time.Clock()

# Internal Variable for calling movement function from main
player = Player()

# Call for drawing Objects

#Scene = Objects(Screen)

""" App close system Loop """
while True:
    # Look for event quit
    for event in pygame.event.get():
         # if "quit" is pressed, app will quit
        if event.type == pygame.QUIT:
            # Kill Game
            exit()
            
    # call movement function (Calls for detected keys) 
    player.movement()
    
    #Screen fill color, uses AppSettings Color Scheme "Black"
    Screen.fill(Color2)
    
    # Ground Drawing
    pygame.draw.rect(Screen, Color4, (0, half_y, x, half_y))
    
    # Scenario display
    ray_casting(Screen, player.pos, player.angle)
    
    # Displays what was rendered
    pygame.display.flip()
    
    # Game FPS Standard 60 FPS
    clock.tick(FPS)
   
            