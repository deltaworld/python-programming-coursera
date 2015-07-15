# Counter ticks
# http://www.codeskulptor.org/#exercises_timers_counter_template.py

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def tick():
    print counter
    counter += 1

# create timer
timer = simplegui.create_timer(1000, tick)


