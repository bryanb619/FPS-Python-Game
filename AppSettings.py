"""General settings and data variables for game configuration"""

# Modules
import math

"""Screen Configuration"""

res_x = 1200 # Width resolution
res_y = 800 # Height resolution
# Frames Per Second Base Limiter
FPS = 60 # 60 by default


"""Camera position"""

half_x = res_x // 2
half_y = res_y // 2


"""Game Mapping"""  

# Walls
walls = 100
#
box = 50


""" Ray Casting settings"""

# Player Point of View
pView = math.pi / 3

# Half Point of View
half_pView = pView / 2

# Depth and Angle
number_rays = 120
max_depth = 800

angle = pView / number_rays

# Object Distance Configuration
dist = number_rays / (3 * math.tan(half_pView))

# Projection 3D 
proj_3d = 3 * dist * walls

# Scale Distance
scale = res_x // number_rays

# player settings
player_pos = (half_x, half_y)


"""RGB Color CODES"""

# Base colors 
Color1 = (255, 255, 255) # White
Color2 = (0, 0, 0) # Black

# Other collors
Color3 = (0,220,0) # Green
Color4 = (128,128,128) # Gray
Color5 = (0,0,204) # Blue
Color6 = (102, 255, 102) # Unused Green
Color7 = (23, 54, 5) # Dark Green
Color8 = (53, 81, 93) # Sky blue 

# Color9 =
