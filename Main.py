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


"""Pygame Window initialization"""

# initiates Game Window
pygame.init()

# Sets Window caption
pygame.display.set_caption("FPS Game Triple Zero")

""" Screen  """
 
# Width = X(1200), Height = Y(800)
Screen = pygame.display.set_mode((res_x, res_y))

# Hides mouse cursor (still there but invisible)
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

# Screen frames
clock = pygame.time.Clock()

# Internal Variable for calling movement function from main
player = Player()

""" App close system Loop """

while True:
    # Look for event quit
    for event in pygame.event.get():
         # if "quit" is pressed, app will quit
        if event.type == pygame.QUIT:
            # Kill Game
            quit()
            
    """Player, Ground and display config  """       
     
    # call movement function (Calls for detected keys) 
    player.movement()
    
    #Screen fill color, uses AppSettings Color Scheme "Black"
    Screen.fill(Color2)
    
    # Ground Drawing
    pygame.draw.rect(Screen, Color4, (0, half_y, res_x, half_y))
    
    # Sky drawing (skyblue)
    pygame.draw.rect(Screen, Color8, (0, 0, res_x, half_y))
    
    # Scenario display
    ray_casting(Screen, player.pos, player.angle)
    
    # Displays what was rendered
    pygame.display.flip()
    
    # Game FPS Standard 60 FPS (calls back for AppSettings.py "FPS")
    clock.tick(FPS)
   
            