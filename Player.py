# PLAYER FILE, Movements, 


# import settings
from AppSettings import * 
# Pygame import
import pygame
# for mathematics
import math

# player coordinates and direction
class PlayerMovement:
    def __init__(self):
        self.x, self.y = playerPosition
        self.angle = playerAngle
        
    # Return    
    @property
    def position(self):
        return (self.x, self.y)
        
    # Movement and walk key detection
    def movement(self):
        
        # sine & cosine for 3D movement
        sin_m = math.sin(self.angle)
        cos_m = math.cos(self.angle)
        
        
        # Key List
        keys = pygame.key.get_pressed()
        # Movements 
        
        # Forward
        if keys[pygame.K_w]:
            self.x += playerSpeed * cos_m
            self.y += playerSpeed * sin_m

        # Back
        if keys[pygame.K_s]:
            self.x -= playerSpeed * cos_m
            self.y += -playerSpeed * sin_m
        # Left    
        if keys[pygame.K_a]:
            self.x += playerSpeed * sin_m
            self.y += -playerSpeed * cos_m
        # Right   
        if keys[pygame.K_d]:
            self.x += -playerSpeed * sin_m
            self.y += playerSpeed * cos_m
                       
        # Optional Keys (Arrow keys)
    
        # Left   
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        # Right       
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
            
        
