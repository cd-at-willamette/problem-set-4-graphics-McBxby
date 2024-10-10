############################################################
# Name: Myles Crandall
# Name(s) of anyone worked with: n/a
# Est time spent (hr): 3.0
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel, GPolygon

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 400
w = WIDTH
h = HEIGHT

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!
    
    # South Africa flag
    
    # Red rectangle
    red_rect = GRect(0, 0, w, h // 2) # x, y, width, height
    red_rect.set_filled(True) # Fills the rectangle with color
    red_rect.set_color('#E03C31') # Sets the color of the rectangle
    gw.add(red_rect) # Adds the rectangle to the window
    
    # Blue rectangle
    blue_rect = GRect(0, 200, w, h // 2) # x, y, width, height
    blue_rect.set_filled(True) # Fills the rectangle with color
    blue_rect.set_color('#001489') # Sets the color of the rectangle
    gw.add(blue_rect) # Adds the rectangle to the window
    
    # White rectangle
    white_rect = GRect(0, h // 3, w, h // 3) # x, y, width, height
    white_rect.set_filled(True) # Fills the rectangle with color
    white_rect.set_color('#FFFFFF') # Sets the color of the rectangle
    gw.add(white_rect) # Adds the rectangle to the window
    
    # White triangle
    white_triangle = GPolygon() # Creates a polygon
    white_triangle.add_vertex(425, 200) # Adds the vertices of the triangle point
    white_triangle.add_vertex(0, 475) # Adds the vertices of the triangle left side
    white_triangle.add_vertex(0, -75) # Adds the vertices of the triangle right side
    white_triangle.set_filled(True) # Fills the triangle with color
    white_triangle.set_color('#FFFFFF') # Sets the color of the triangle
    gw.add(white_triangle) # Adds the triangle to the window
    
    # Green rectangle
    green_rect = GRect(0, h // 2.5, w, h // 5) # x, y, width, height
    green_rect.set_filled(True) # Fills the rectangle with color
    green_rect.set_color('#007749') # Sets the color of the rectangle
    gw.add(green_rect) #  Adds the rectangle to the window
    
    # Green triangle
    green_triangle = GPolygon() # Creates a polygon
    green_triangle.add_vertex(375, 200) # Adds the vertices of the triangle point
    green_triangle.add_vertex(0, 450) # Adds the vertices of the triangle left side
    green_triangle.add_vertex(0, -50) # Adds the vertices of the triangle right side
    green_triangle.set_filled(True) # Fills the triangle with color
    green_triangle.set_color('#007749') #  Sets the color of the triangle
    gw.add(green_triangle) # Adds the triangle to the window
    
    # Yellow triangle
    yellow_triangle = GPolygon() # Creates a polygon
    yellow_triangle.add_vertex(225, 200) # Adds the vertices of the triangle point
    yellow_triangle.add_vertex(0, 40) # Adds the vertices of the triangle left side
    yellow_triangle.add_vertex(0, 360) # Adds the vertices of the triangle right side
    yellow_triangle.set_filled(True) # Fills the triangle with color
    yellow_triangle.set_color('#FCB514') # Sets the color of the triangle
    gw.add(yellow_triangle) # Adds the triangle to the window
    
    # Black triangle
    black_triangle = GPolygon() # Creates a polygon
    black_triangle.add_vertex(175, 200) # Adds the vertices of the triangle point
    black_triangle.add_vertex(0, 75) # Adds the vertices of the triangle left side
    black_triangle.add_vertex(0, 325) # Adds the vertices of the triangle right side
    black_triangle.set_filled(True) # Fills the triangle with color
    black_triangle.set_color('#000000') # Sets the color of the triangle
    gw.add(black_triangle) # Adds the triangle to the window
    
if __name__ == '__main__':
    draw_image()
