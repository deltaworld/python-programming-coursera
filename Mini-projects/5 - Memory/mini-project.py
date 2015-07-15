# implementation of card game - Memory
# http://www.codeskulptor.org/#user14_REpDdR0Qis_3.py

import simplegui
import random
HEIGHT = 100
# global variables
state = 0
cards = [3, 15]
l1 = range(8)
l2 = range(8)
lists = l1 + l2
exposed = []
matched = []
counter = 0



# helper function to initialize globals
def init():
    global state, matched, counter, exposed
    state = 0
    matched = []
    exposed = []
    counter = 0
    random.shuffle(lists)
    label.set_text("Moves = " + str(counter))
    for x in range(len(lists)):
        exposed.append(False)
    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, counter
    card = pos[0] // 50
    if exposed[card] != True:
        counter = counter + 1
        print counter
        label.set_text("Moves = " + str(counter))
    
        cards.pop(0)
        cards.append(card)
        if state == 0:
            state = 1
        elif state == 1:
            state = 2
        elif state == 2:
            # check for pairs
        
            
            for x in range(len(lists)):
                exposed[x] = False
            
             
            state = 1
        
        if exposed[card] != True:
            if lists[cards[0]] == lists[cards[1]]:
                print "MATCH", lists[cards[0]], cards
                matched.append(cards[0])
                matched.append(cards[1])
                print "matched", matched
            print card
            exposed[card] = True
        
        print cards

# cards are logically 50x100 pixels in size    
def draw(canvas):
    #for x in lists:
    for x in range(16):
        if exposed[x] == True:
            canvas.draw_text(str(lists[x]), (x * 50, 85), HEIGHT, "White")
        else:
            canvas.draw_polygon([(x * 50, 0), (50 + x * 50 , 0), (50 + x * 50 , HEIGHT), (x * 50 , HEIGHT)], 1, "Black", "Green")
    for x in matched:
        exposed[x] = True
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, HEIGHT)
frame.add_button("Restart", init)
label = frame.add_label("Moves = " + str(counter))

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)

# list shuffler method
random.shuffle(lists)

frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric