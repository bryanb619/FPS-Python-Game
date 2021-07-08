"Ray Settings File"

# Modules
import pygame, math
# File Imports
# Settings
from AppSettings import *
# Mapping
from Map import GameMap

""" Raycasting """
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
                proj_height = proj_3d / depth
                c = 255 / (1 + depth * depth * 0.00002)
                Shade = (c, c // 2, c // 3)
                
                """ Walls insertion drawing"""
                pygame.draw.rect(Screen, Shade, (ray * scale, half_x - proj_height // 2, scale, proj_height))
                # Read once this if, so break it ( CORRIGIR)
                break
        """    
        cur_angle += angle
        def mapping(a, b):
            return (a // walls) * walls, (b // walls) * walls
        
        def ray_casting (Screen, player_pos, player_angle):
            ox, oy = player_pos
            xm, ym  = mapping(ox, oy)
            cur_angle = - half_pView
            
            for ray in range(number_rays):
                sin_a = math.sin(cur_angle)
                cos_a = math.cos(cur_angle)
                
                x, dx = (xm + walls, 1) if cos_a >= 0 else (xm, -1)
                    
                for i in range(0 , X, walls):
                    depthRay = (x -ox) / cos_a
                    y = oy + depthRay + sin_a
                    if mapping(x + dx, y) in GameMap:
                        break
                    x += dx * walls
                
                # horizontal 
                for j in range(0, Y, walls): """
                    
            

