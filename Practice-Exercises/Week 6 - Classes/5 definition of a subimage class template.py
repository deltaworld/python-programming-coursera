# Implementation of Subimage class
# http://www.codeskulptor.org/#exercises_classes_subimage_def_template.py


#################################################
# Student adds code where appropriate

# definition of Subimage class
class Subimage:
    
    def __init__(self, image, center, size, caption):
        
    def draw(self, canvas, target):
   
    def get_caption(self):
    
    def set_caption(self, new_caption):
        
    
    
###################################################
# Testing code

import simplegui

instructor_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/instructors.jpg")

# create a Subimage object
john_image = Subimage(instructor_image, [500, 150], [200, 200], "John")

def draw(canvas):
    john_image.draw(canvas, [100, 100])
    
    
frame = simplegui.create_frame("Subimage test", 200, 200)
frame.set_draw_handler(draw)
frame.start()

# test code for get_caption and set_caption
print john_image.get_caption()
john_image.set_caption("Greiner")
print john_image.get_caption()
john_image.set_caption("Rocks!")
print john_image.get_caption()



####################################################
# Output  - should see a picture of John with caption "Greiner"

#John
#Greiner
#Greiner


