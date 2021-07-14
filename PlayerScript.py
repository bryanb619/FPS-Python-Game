""" Player file """

# Modules
import pygame
# Automatic Module import
from pygame.constants import K_LSHIFT

# import settings
from AppSettings import *

""" Player Settings """

# Angle
player_angle = 0  # Horizontal

# Speed
player_speed = 1  # Horizontal Speed

PlayerSide = 1
PlayerBack = 1

# Sprint speed
Sprint = 1.3  # Horizontal sprinting speed

# player does not jump from beginning, so False
# isJumping = False # will be changed to true as soon as "SPACE" is hit

# Jump Timer
# CounterJ = 10


""" Player Main Class """


class Player:
    def __init__(self):
        # X & Y player position
        self.x, self.y = player_pos
        # Player angle (rotation)
        self.angle = player_angle

    # Self return
    @property
    def pos(self):
        return self.x, self.y

    """ Movement function (Detects pressed Keys) """

    def movement(self):
        # Movement math
        sin = math.sin(self.angle)
        cos = math.cos(self.angle)

        """ Keyboard detection """
        buttons = pygame.key.get_pressed()

        # Special movements

        # Forward and Sprint "w + Left Shift"
        if buttons[pygame.K_w & K_LSHIFT]:
            self.x += (Sprint + player_speed) * cos
            self.y += (Sprint + player_speed) * sin

        # General Movement

        # Forward "k"
        if buttons[pygame.K_w]:
            self.x += player_speed * cos
            self.y += player_speed * sin
        # Back "s"
        if buttons[pygame.K_s]:
            self.x += -player_speed * cos
            self.y += -player_speed * sin
        # Left "a"
        if buttons[pygame.K_a]:
            self.x += player_speed * sin
            self.y += -player_speed * cos

        # Right "d"   
        if buttons[pygame.K_d]:
            self.x += -player_speed * sin
            self.y += player_speed * cos

            # Left Rotation  "Left Arrow"
        if buttons[pygame.K_LEFT]:
            self.angle -= 0.02

            # Right Rotation "Right Arrow"
        if buttons[pygame.K_RIGHT]:
            self.angle += 0.02

        #   UI Controls  

        # Quit Game "ESC"
        if buttons[pygame.K_ESCAPE]:
            quit()

        """ Mouse detection"""

        # if not(isJumping):
        # Jump "Backspace"
        # if buttons[pygame.K_SPACE]:
        # Jump is now true
        # isJumping = True

    # Rotation (TO UPDATE TO MOUSE!)

    # Mouse Controls
