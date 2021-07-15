"""Ray Settings File"""

# Modules, PYGAME & MATH
import pygame, math

# Settings
from AppSettings import *
# Mapping
from Map import GameMap


# Game Mapping
def GameMapping(j, i):
    return (j // walls) * walls, (i // walls) * walls

"""Raycasting """
def ray_casting(Screen, player_pos, player_angle):
    
    ox, oy = player_pos
    xx, yy = GameMapping(ox, oy)
    cur_angle = player_angle - half_pView
    
    # Ray apply
    for ray in range(number_rays):
        sin_x = math.sin(cur_angle)
        cos_x = math.cos(cur_angle)

        sin_x = sin_x if sin_x else 0.000002
        cos_x = cos_x if cos_x else 0.000002

        # verticals rays
        x, dx = (xx + walls, 1) if cos_x >= 0 else (xx, -1)
        
        for i in range(0, res_x, walls):
            depth_v = (x - ox) / cos_x
            y = oy + depth_v * sin_x
            
            if GameMapping(x + dx, y) in GameMap:
                break
            x += dx * walls

        # horizontals rays
        y, dy = (yy + walls, 1) if sin_x >= 0 else (yy, -1)
        
        
        for i in range(0, res_y, walls):
            
            depth_h = (y - oy) / sin_x
            x = ox + depth_h * cos_x
            if GameMapping(x, y + dy) in GameMap:
                break
            y += dy * walls

        # 3D projection Depth Adaptation
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        
        # Depth darkness
        proj_height = proj_3d / depth
        
        # Depth of walls
        c = 135 / (1 + depth * depth * 0.00002)
        DepthColor = (c, c // 2, c // 3)
        
        # Walls drawing
        pygame.draw.rect(Screen, DepthColor, (ray * scale, half_y - proj_height // 2, scale, proj_height))
        cur_angle += angle