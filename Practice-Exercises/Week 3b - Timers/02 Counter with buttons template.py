# Counter with buttons
# http://www.codeskulptor.org/#exercises_timers_buttons_template.py

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
# Event handlers for buttons    

        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()
