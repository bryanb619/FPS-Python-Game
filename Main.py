# Main FILE

# imports

# Pygame import
import pygame 
# import settings from AppSettings.py
from AppSettings import * 
# import player Settings from App Settings
from Player import PlayerMovement
# Import Game Map
from Map import GameWorld
# for mathematics
import math
# import Ray Casting from Ray.py
from Ray import RayCasting

# Window initialization
pygame.init()

# Display set (Width & Height)
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
    # in Player.py get movement function (keys) 
    Player.movement()
    #Screen fill color, uses AppSettings Color Scheme
    ss.fill(Black)
    
    #
    RayCasting(ss, Player.position, Player.angle)
    
    # Player (for the moment!)
    pygame.draw.circle(ss,Green,(int(Player.x), int(Player.y)),12)
    
    #  Line 
    pygame.draw.line(ss, Green, Player.position,(Player.x + Width * math.cos(Player.angle),Player.y + Width * math.sin(Player.angle)))
    
    # Map Drawing
    for x,y in GameWorld:
        pygame.draw.rect(ss, Gray, (x,y, Tile, Tile), 2)
    
    # 
    pygame.display.flip()
    # Game FPS Standard 60 FPS
    clock.tick(Fps)
    
    
            