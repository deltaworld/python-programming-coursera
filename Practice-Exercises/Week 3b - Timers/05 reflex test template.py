# Reflex tester
# http://www.codeskulptor.org/#exercises_timers_reflex_template.py

###################################################
# Student should add code where relevant to the following.

import simplegui 

total_ticks = 0
first_click = True


# Timer handler

    
# Button handler


# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
timer.start()
