# Counter with buttons
# http://www.codeskulptor.org/#exercises_timers_toggle_template.py

###################################################
# Student should add code where relevant to the following.

import simplegui 

color = "Red"


# Timer handler
def tick():
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()
