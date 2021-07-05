# General settings and data variables for game configuration

#
import math

# Screen Settings
Width =1200 # Width of screen
Height = 800 # Height of screen
# Frames per second
Fps = 60
# Game Tiles
Tile = 100

# Centering player
HalfWidth = Width // 2  
HalfHeight = Height // 2

# Player Settings
playerPosition = (HalfWidth, HalfHeight)
#
playerAngle = 0
# speed
playerSpeed = 2

# Casting Settings

# Player field of view
pView = math.pi / 3
#
HalfView = pView / 2
# Number of rays
rays = 120
# delta = field of view / rays
deltaAngle = pView / rays
# Maximum Depth
FullDepth = 800

# Colors (RGB CODES)

Black = (0,0,0) # Black
White = (255,255,255) # White

# Other collors
Green = (0,220,0) # Green
Gray = (128,128,128) # Gray