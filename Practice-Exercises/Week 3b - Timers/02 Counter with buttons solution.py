# Counter with buttons
# http://www.codeskulptor.org/#exercises_timers_buttons_solution.py

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
def start():
    timer.start()
    
def stop():
    timer.stop()

def reset():
    global counter
    counter = 0
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()
