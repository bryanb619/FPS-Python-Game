"""Ray Settings File"""

# Modules
import pygame, math

# Settings
from AppSettings import *
# Mapping
from Map import GameMap



def mapping(a, b):
    return (a // walls) * walls, (b // walls) * walls

"""Raycasting """
def ray_casting(sc, player_pos, player_angle):
    
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - half_pView
    
    for ray in range(number_rays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals rays
        x, dx = (xm + walls, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, res_x, walls):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in GameMap:
                break
            x += dx * walls

        # horizontals rays
        y, dy = (ym + walls, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, res_y, walls):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in GameMap:
                break
            y += dy * walls

        # 3D projection Adaptation
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        proj_height = proj_3d / depth
        
        # Depth of walls
        c = 135 / (1 + depth * depth * 0.00002)
        color = (c, c // 2, c // 3)
        # Walls
        pygame.draw.rect(sc, color, (ray * scale, half_y - proj_height // 2, scale, proj_height))
        cur_angle += angle



"""def ray_casting(Screen, player_pos, player_angle):
    
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
                c = 124 / (1 + depth * depth * 0.00002)
                Shade = (c, c // 2, c // 3)
                
                #Walls insertion drawing
                pygame.draw.rect(Screen, Shade, (ray * scale, half_y - proj_height // 2, scale, proj_height))
                # Read once this if, so break it ( CORRIGIR)
                break           
    
        cur_angle += angle """