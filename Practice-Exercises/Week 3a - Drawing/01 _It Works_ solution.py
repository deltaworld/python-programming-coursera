# Print to canvas
# http://www.codeskulptor.org/#exercises_drawing_works_solution.py

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    canvas.draw_text("It works!",[120, 112], 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("It works", 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()

