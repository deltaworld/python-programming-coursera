# Open a frame
# http://www.codeskulptor.org/#exercises_intapp_open_frame_template.py

###################################################
# Open frame
# Student should add code where relevant to the following.

import simplegui 

message = "My second frame!"

# Handler for mouse click
def click():
    print message

# Assign callbacks to event handlers
frame.add_button("Click me", click)

# Start the frame animation
frame.start()

