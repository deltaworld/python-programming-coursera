# Image debugging problem
# http://www.codeskulptor.org/#exercises_dictionaries_debug_template.py

###################################################
# Student should enter code below

import simplegui

# load test image
test_image = load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png")
test_image_size = [135, 164]
test_image_center = [test_image_size[0] / 2, test_image_size[1] / 2]

# draw handler
def draw(canvas):
    canvas.draw_image(test_image, test_image_center, test_image_size, 
                      test_image_center, [0, 0])

# create frame and register draw handler    
frame = simplegui.create_frame("Test image", test_image_size[0], test_image_size[1])


# start frame
frame.start()
        
                                       