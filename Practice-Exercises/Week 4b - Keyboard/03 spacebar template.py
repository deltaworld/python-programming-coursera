# Space bar status
# http://www.codeskulptor.org/#exercises_keyboard_spacebar_template.py

import simplegui

message = "Space bar up"

# Handlers for keydown and keyup
def keydown(key):
    global message

    # add code here


def keyup(key):
    global message

    # add code here 


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [25, 112], 42, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
