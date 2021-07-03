# PLAYER FILE

# import settings
from AppSettings import * 
# Pygame import
import pygame

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
        
        # Key List
        keys = pygame.key.get_pressed()
        # Movements 
        
        # Forward
        if keys[pygame.K_w]:
            self.y -= playerSpeed   
        # Back
        if keys[pygame.K_s]:
            self.y += playerSpeed
        # Left    
        if keys[pygame.K_a]:
            self.x -= playerSpeed
        # Right   
        if keys[pygame.K_d]:
            self.x += playerSpeed
                       
        # Optional Keys (Arrow keys)
    
        # Left   
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        # Right       
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
            
        
