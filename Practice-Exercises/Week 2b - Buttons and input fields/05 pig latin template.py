# Convert input text into Pig Latin
# http://www.codeskulptor.org/#exercises_button_pig_latin_template.py

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.

# Handler for input field
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)


# Start the frame animation
frame.start()



###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay


