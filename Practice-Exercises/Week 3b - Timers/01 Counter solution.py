# Counter ticks
# http://www.codeskulptor.org/#exercises_timers_counter_solution.py

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1

# create timer
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()

