# General settings and data variables for game configuration

# Biblioteca Math
import math

"""Screen Configuration"""

x = 800 # Width
y = 600 # Height

# Frames Per Second
FPS = 60 

"""Camera position"""

half_x = x // 2
half_y = y // 2

"""Game Mapping""" 

# Walls
walls = 100

""" Ray Casting Settings"""

# Player Point of View
pView = math.pi / 3

# Half Point of View
half_pView = pView / 2

# Depth and Angle
number_rays = 80
max_depth = 800
angle = pView / number_rays

# Object Distance Configuration
dist = number_rays / (2 * math.tan(half_pView))

# Projection 3D
proj_3d = 3 * dist * walls

# Scale Distance
scale = x // number_rays

# Player Position
player_pos = (half_x, half_y)


"""RGB CODES"""

# Base colors 
Color1 = (255, 255, 255) # White
Color2 = (0, 0, 0) # Black

# Other colors
Color3 = (0,220,0) # Green
Color4 = (128,128,128) # Gray
Color5 = (0,0,204) # Blue
Color6 = (102, 255, 102) # Unused Green
Color7 = (23, 54, 5) # Dark Green
