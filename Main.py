"""Main FILE"""

# Python Modules
import pygame

# File import
# Game Main Settings file
from AppSettings import *
# import player Settings from PlayerScript
from PlayerScript import Player
# Import Ray Casting from Ray.py
from Ray import ray_casting

# Import Game Map

"""Pygame Window initialization"""

# initiates Game Window
pygame.init()

# Sets Window caption
pygame.display.set_caption("FPS Application Like")

# Hides mouse cursor ( still there but invisible)
pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

""" Screen  """

# Width = X(800), Height = Y(600)
Screen = pygame.display.set_mode((res_x, res_y))

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

    # Screen fill color, uses AppSettings Color Scheme "Black"
    Screen.fill(Color2)

    # Ground Drawing
    pygame.draw.rect(Screen, Color4, (0, half_y, res_x, half_y))

    # Sky drawing
    pygame.draw.rect(Screen, Color8, (0, 0, res_x, half_y))

    # Scenario display
    ray_casting(Screen, player.pos, player.angle)

    # Displays what was rendered
    pygame.display.flip()

    # Game FPS Standard 60 FPS
    clock.tick(FPS)
