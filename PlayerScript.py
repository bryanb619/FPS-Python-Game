" Player file "

# Modules
import pygame, math
# import settings
from AppSettings import *

" Player Settings "
# Angle
player_angle = 0 # Horizontal
# Speed
player_speed = 1 # Horizontal Speed

" Player Main Class "
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
    
    " movement function (Detects pressed Keys) "
    def movement(self):
        # Movement math
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        
        " Key detection "
        keys = pygame.key.get_pressed()
        # Forward
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        # Back
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        # Left
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        # Right   
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a  
            
        # Rotation (TO UPDATE TO MOUSE!)  
        # Left Rotation  
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02 
        # Right Rotaion
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
            
        " Key List Mouse" # (TO BE FIXED) 
        mx, my = pygame.mouse.get_pos()

        # Mouse Control Variables
        left_click = False
        right_click = False

        # Mouse Controls

