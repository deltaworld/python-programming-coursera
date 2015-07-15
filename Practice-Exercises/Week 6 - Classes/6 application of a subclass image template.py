# Application of Subimage class
# http://www.codeskulptor.org/#exercises_classes_subimage_use_template.py


# definition of Subimage class
class Subimage:
    
    def __init__(self, image, center, size, caption):
        self.image = image
        self.image_center = center
        self.image_size = size
        self.caption = caption
        self.modified = False
        
    def draw(self, canvas, target):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          target, self.image_size)
        canvas.draw_text(self.caption, [target[0] - self.image_size[0] * 0.25, target[1] + self.image_size[1] * 0.4], 18, "White")
    
    def get_caption(self):
        return self.caption
    
    def set_caption(self, new_caption):
        if not self.modified:
            self.caption = new_caption
            self.modified = True
        
    
    
###################################################
# Student adds code as necessary below

import simplegui

#load big image
instructor_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/instructors.jpg")

# create a Subimage objects


# define button handlers
def joe_button():

def scott_button():

def john_button():

def stephen_button():
  
def awesome_button():

# draw handler
def draw(canvas):
    
    
frame = simplegui.create_frame("Subimage application", 200, 200)
frame.add_button("Joe", joe_button, 100)
frame.add_button("Scott", scott_button, 100)
frame.add_button("John", john_button, 100)
frame.add_button("Stephen", stephen_button, 100)
frame.add_button("Make awesome", awesome_button, 200)

frame.set_draw_handler(draw)
frame.start()




