# General settings and data variables for game configuration

<<<<<<< HEAD
<<<<<<< HEAD
# Modules
import math


"""Screen Configuration"""

x = 800 # Width
y = 600 # Height
# Frames Per Second Limit
FPS = 60 


"""Camera position"""

half_x = x // 2
half_y = y // 2


"""Game Mapping"""  
=======
# Biblioteca Math
import math

"""Screen Configuration"""

x = 800 # Width
y = 600 # Height

# Frames Per Second
FPS = 60 

"""Camera position"""

=======
# Biblioteca Math
import math

"""Screen Configuration"""

x = 800 # Width
y = 600 # Height

# Frames Per Second
FPS = 60 

"""Camera position"""

>>>>>>> origin/main
half_x = x // 2
half_y = y // 2

"""Game Mapping""" 
<<<<<<< HEAD
>>>>>>> origin/main
=======
>>>>>>> origin/main

# Walls
walls = 100

<<<<<<< HEAD
<<<<<<< HEAD

""" Ray Casting settings"""
=======
""" Ray Casting Settings"""
>>>>>>> origin/main
=======
""" Ray Casting Settings"""
>>>>>>> origin/main

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

<<<<<<< HEAD
<<<<<<< HEAD
# player settings
player_pos = (half_x, half_y)


"""RGB Color CODES"""
=======
=======
>>>>>>> origin/main
# Player Position
player_pos = (half_x, half_y)


"""RGB CODES"""
<<<<<<< HEAD
>>>>>>> origin/main
=======
>>>>>>> origin/main

# Base colors 
Color1 = (255, 255, 255) # White
Color2 = (0, 0, 0) # Black

<<<<<<< HEAD
<<<<<<< HEAD
# Other collors
=======
# Other colors
>>>>>>> origin/main
=======
# Other colors
>>>>>>> origin/main
Color3 = (0,220,0) # Green
Color4 = (128,128,128) # Gray
Color5 = (0,0,204) # Blue
Color6 = (102, 255, 102) # Unused Green
Color7 = (23, 54, 5) # Dark Green
<<<<<<< HEAD
<<<<<<< HEAD
# Color8 = 
# Color9 =
=======
>>>>>>> origin/main
=======
>>>>>>> origin/main
