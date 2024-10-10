########################################
# Name: Myles Crandall
# Collaborators: n/a
# Estimate time spent (hrs): 3.5
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score
w = GW_WIDTH
h = GW_HEIGHT
ss = SQUARE_SIZE
sx = SCORE_DX
sy = SCORE_DY
sf = SCORE_FONT

gw = GWindow(GW_WIDTH, GW_HEIGHT)

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'brown', 'cyan', 'magenta', 'pink', 'lime', 'teal', 'navy', 'olive', 'maroon', 'aqua', 'fuchsia', 'silver', 'gold', 'indigo', 'coral', 'lavender', 'salmon', 'turquoise', 'plum', 'tan', 'khaki', 'crimson', 'orchid', 'sienna', 'peru', 'darkgreen', 'darkblue', 'darkred', 'darkorange', 'darkcyan', 'darkmagenta', 'darkviolet', 'darkkhaki', 'darkslategray', 'darkolivegreen', 'darkgoldenrod', 'darkorchid', 'darkslateblue', 'darkturquoise', 'darkviolet', 'darkred', 'darkorange', 'darkcyan', 'darkmagenta', 'darkviolet', 'darkkhaki', 'darkslategray', 'darkolivegreen', 'darkgoldenrod', 'darkorchid', 'darkslateblue', 'darkturquoise', 'darkviolet', 'darkred', 'darkorange', 'darkcyan', 'darkmagenta', 'darkviolet', 'darkkhaki', 'darkslategray', 'darkolivegreen', 'darkgolden']

def clicky_box():
    
    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function
    
    def change_color():
        new_color = random.choice(COLORS) # Randomly chooses a color from the list of colors
        gw.box.set_filled(True) # Fills the square
        gw.box.set_color(new_color) # Sets the color of the square to the new color
        
    gw.box = GRect((w - ss) // 2, (h - ss) // 2, ss, ss) # Creates a square in the center of the GWindow
    gw.add(gw.box) # Adds the square to the GWindow
    
    score_label = GLabel("0") # Creates a label for the score
    score_label.set_font(sf) # Sets the font of the label
    gw.add(score_label, sx, h - sy) # Adds the label to the GWindow
    
    # Defining the callback function, which you won't need until Part C
    
    def on_mouse_down(event):
        element = gw.get_element_at(event.get_x(), event.get_y()) # Gets the element at the mouse click
        if element == gw.box: # If the element is the square
            move_square() # Moves the square
            change_color() # Changes the color of the square
            score = int(score_label.get_label()) + 1 # Increment the score
            score_label.set_label(str(score)) # Set's the label of the label to the score
        else: # If the element is not the square
            score_label.set_label("0") # Set the label of the label to 0
            
    def move_square():
        x = random.randint(0, w - ss) # Random x coordinate
        y = random.randint(0, h - ss) # Random y coordinate
        gw.box.set_location(x, y) # Set's the location of the square to the random coordinates staying in the GWindow
    
    gw.add_event_listener("click", on_mouse_down)

if __name__ == '__main__':
    clicky_box()
