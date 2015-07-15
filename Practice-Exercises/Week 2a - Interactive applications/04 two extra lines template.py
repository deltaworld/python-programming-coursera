# Open a frame
# http://www.codeskulptor.org/#exercises_intapp_twoline_template.py

###################################################
# Open frame
# Student should add code where relevant to the following.


message = "My first frame!"

# Handler for mouse click
def click():
    print message

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)


