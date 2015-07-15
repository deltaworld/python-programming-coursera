# implementation of card game - Memory
# http://www.codeskulptor.org/#user14_yXuoXs6ybZ0HAkI.py
import simplegui
import random
deck = []
width = 800
height = 100
exposed = []
state = 0
num_card = 0
last_card = [] 
last_pos = []
moves = 0
# helper function to initialize globals
def init():
    global moves, state, deck, exposed, last_card, last_pos, num_card
    moves = 0
    label.set_text("Moves = " + str(moves))
    state = 0
    deck = []
    exposed = []
    last_card = [] 
    last_pos = []
    num_card = 0
    
    list1 = range(8)
    random.shuffle(list1)
    list2 = range(8)
    random.shuffle(list2)
    num = 0
    for items in list1:
        deck.append(list1[num])
        deck.append(list2[num])
        num += 1
        
    for cards in deck:
        exposed.append(0)
        


     
# define event handlers
def mouseclick(pos):
    global state, num_card, deck, last_card, last_pos, moves
    
    if exposed[pos[0] // 50]:
        pass
    else:
        
        # add game state logic here
        if state == 0:
            num_card = pos[0] // 50
            last_card.append(deck[num_card])
            last_pos.append(num_card)
            exposed[num_card] = 1
            state = 1
            
        elif state == 1:
            moves += 1
            label.set_text("Moves = " + str(moves))
            num_card = pos[0] // 50
            last_card.append(deck[num_card])
            last_pos.append(num_card)
            exposed[num_card] = 1
            state = 2
            
        else:
            
            if deck[int(last_pos[-1])] == deck[int(last_pos[-2])]:
                num_card = pos[0] // 50
                last_card.append(deck[num_card])
                last_pos.append(num_card)
                exposed[num_card] = 1
                state = 1 
            else:
                num_card = pos[0] // 50
                last_card.append(deck[num_card])
                last_pos.append(num_card)
                exposed[num_card] = 1
                exposed[int(last_pos[-2])] = 0
                exposed[int(last_pos[-3])] = 0
                state = 1
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, state, num_card
    x = 0
   
    for cards in deck:
        if  exposed[x]:
            canvas.draw_text(str(deck[x]), [(width // 32) - 12 + (width // 16) * x, height // 1.5], 48, "red")
            x += 1
        else:
            
            canvas.draw_polygon([(0 + 50 * x, 0), (50 + 50 * x, 0), (50 + 50 * x, height),(0 + 50 * x, height)], 1,  "red", "aqua")

            x += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")


# initialize global variables
init()


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric