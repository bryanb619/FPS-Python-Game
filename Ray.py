"""Ray Settings File"""

# Modules
import pygame, math
# File Imports
# Settings
from AppSettings import *
# Mapping
from Map import GameMap

"""Raycasting """
 
def ray_casting(Screen, player_pos, player_angle):
    
    cur_angle = player_angle - half_pView
    
    # Inicial Player position of casting
    xo, yo = player_pos
    
    # Display of raycast
    for ray in range(number_rays):
        
        # Math for rays
        sin_a = math.sin(cur_angle) #
        cos_a = math.cos(cur_angle) #
        
        # Depth View
        for depth in range(max_depth):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            
            # Walls inserting with raycasting
            if (x // walls * walls, y // walls * walls) in GameMap:
                
                # Apply Darkness depth for walls
                depth *= math.cos(player_angle - cur_angle)
                proj_height = proj_3d / depth
                c = 255 / (1 + depth * depth * 0.00002)
                Shade = (c, c // 2, c // 3)
                
                """Walls insertion drawing"""
                pygame.draw.rect(Screen, Shade, (ray * scale, half_y - proj_height // 2, scale, proj_height))
                # Read once this if, so break it ( CORRIGIR)
                break
        cur_angle += angle
       
"""def mapping(a, b):
    return (a // walls) * walls, (b // walls) * walls
        
def ray_casting (Screen, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym  = mapping(ox, oy)
    cur_angle = - half_pView
            
    for ray in range(number_rays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
                
        # Vertical
        X, dx = (xm + walls, 1) if cos_a >= 0 else (xm, -1)
                    
        for i in range(0 , x, walls):
            depthVertical = (X -ox) / cos_a
            Y = oy + depthVertical + sin_a
            if mapping(X + dx, Y) in GameMap:
                break
            X += dx * walls
                
        # horizontal 
        Y, dy = (ym + walls, 1) if sin_a >=0 else (ym, -1)
        for i in range(0, y, walls): 
            depthHoz = (Y - oy) / sin_a
            X = ox + depthHoz * cos_a
                    
            if mapping(X, Y + dy) in GameMap:
                break
            Y += dy * walls
            
        depth = depthVertical if depthVertical < depthHoz else depthHoz
        depth *= math.cos(player_angle - cur_angle)
        proj_height = proj_3d / depth
        c = 255 / (1 + depth * depth * 0.00002)
        Shade = (c, c // 2, c // 3)
                
        "Walls insertion drawing"
        pygame.draw.rect(Screen, Shade, (ray * scale, half_y - proj_height // 2, scale, proj_height))
        cur_angle += angle
"""