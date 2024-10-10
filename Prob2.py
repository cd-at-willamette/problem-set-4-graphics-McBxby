########################################
# Name: Myles Crandall
# Collaborators: n/a
# Estimated time spent (hrs): 2.0
########################################

from pgl import GWindow, GRect
import unittest
from unittest.mock import patch, MagicMock

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15
w = WIDTH
h = HEIGHT
bw = BRICK_WIDTH
bh = BRICK_HEIGHT
bih = BRICKS_IN_BASE

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)

    # You got it from here
    total_height = bh * bih # Total height of the pyramid
    start_y = (h - total_height) // 2 # Start of the pyramid
    n_bricks = 1 # Number of bricks in a row
    
    for i in range(bih): # For each row
        start_x = (w - bw * n_bricks) // 2 # Start of the row
        for j in range(n_bricks): # For each brick in the row
            brick = GRect(start_x + bw * j, start_y + bh * i, bw, bh) # Creates a brick pyramid at the center of the screen 
            brick.set_filled(False) # Set's the bricks to not be filled
            brick.set_color('#cb4154') # Set's the brick outline to be brick red
            gw.add(brick) # Add's the bricks to the GWindow
        n_bricks += 1 # Increment the number of bricks in a row

if __name__ == '__main__':
    draw_pyramid()
