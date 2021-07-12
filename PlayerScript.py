""" Player file """

# Modules
import pygame, math

from pygame.locals import*

# Automatic Module import
from pygame.constants import KEYDOWN, K_DOWN, K_LSHIFT, K_UP

# import settings
from AppSettings import *


""" Player Settings """

# Angle
player_angle = 0 # Horizontal

# Speed
player_speed = 1 # Horizontal Speed

PlayerSide = 1
PlayerBack = 0.2


# Sprint speed
Sprint = 1.3 # Horizontal sprinting speed

# player does not jump from begining, so False
isJumping = False # will be changed to true as soon as "SPACE" is hit

# Jump Timer
CounterJ = 10 


""" Player Main Class """

class Player:
    def __init__(self):
        # X & Y player position
        self.x, self.y = player_pos
        # Player angle (rotaion)
        self.angle = player_angle
        
    # Self return
    @property
    def pos(self):
        return (self.x, self.y)
    
    
    """ Movement function (Detects pressed Keys) """
    
    def movement(self):
        # Movement math
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        
        """ Keyboard detection """
        keys = pygame.key.get_pressed()
        
        
        
        # Special movements   
            
        # Forward and Sprint "w + Left Shift" 
        if keys[pygame.K_w & K_LSHIFT]:
            self.x += Sprint * player_speed * cos_a
            self.y += Sprint * player_speed * sin_a
        
        # General Movement
        
        # Forward "k"
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        # Back "s"
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        # Left "a"
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
            
        # Right "d"   
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a 
            
        # Left Rotation  "Left Arrow"
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02 
            
        # Right Rotaion "Right Arrow"
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
               
        #   UI Controls  
        
        # Quit Game "ESC"
        if keys[pygame.K_ESCAPE]: 
            quit()
            
        
        """ Mouse detection"""

        #if not(isJumping):  
            # Jump "Backspace"
            # if keys[pygame.K_SPACE]:
                    # Jump is now true
                    # isJumping = True
            
            
       # Rotation (TO UPDATE TO MOUSE!)  
    

        # Mouse Controls

