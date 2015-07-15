# Display "This is easy?"
# http://www.codeskulptor.org/#exercises_drawing_easy_template.py

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Draw handler
def draw(canvas):
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()

