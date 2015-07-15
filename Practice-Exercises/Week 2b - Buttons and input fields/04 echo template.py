# Echo an input field
# http://www.codeskulptor.org/#exercises_button_echo_template.py

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Handlers for input field
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_input("First test input")
get_input("Second test input")
get_input("Third test input")

###################################################
# Expected output from test

#First test input
#Second test input
#Third test input
