# implementation of card game - Memory
# http://www.codeskulptor.org/#user14_VlmTzphX1Qt6uxi.py

import simplegui
import random

n = 8 # number of pairs of cards
frame_height = 100
frame_width = 100 * n
font_size = 45

# helper function to initialize globals
def init():
    global deck, exposed, moves, state  
    # set the deck of card knowing number of pairs
    deck = [i % n for i in range(2 * n)]
    random.shuffle(deck) # shuffle the deck of cards
    exposed = [False for i in range(2 *n)] # initializing list with all values False, meaning all cards are facing down. 
    moves = state = 0
    moves_label.set_text("Number of moves = 0")
   
# define event handlers
def mouseclick(pos):
    global deck, exposed, moves, state, position, position_card1, position_card2
    position = pos[0] // 50 # find the position of the clicked card in the list          
    if state == 0: # first click in the game
        exposed[position] = True
        state = 1
        position_card1 = position # position of the first card
        moves += 1 # first card flipped, change number of made moves
        number_moves = "Number of moves = " + str(moves)
        moves_label.set_text(number_moves)
    else:
        if exposed[position] == False and state == 1: # second card open
            exposed[position] = True
            position_card2 = position # position of the second chosen card         
            state = 2           
        elif exposed[position] == False and state == 2: # third card open
            exposed[position] = True
            moves += 1
            number_moves = "Number of moves = " + str(moves)
            moves_label.set_text(number_moves)
            if deck[position_card1] == deck[position_card2]: # cards the same
                exposed[position_card1] = exposed[position_card2] = True # leave open
            else:
                exposed[position_card1] = exposed[position_card2] = False # flip cards  to face down
            position_card1 = position
            state = 1          
           
# cards are logically 50x100 pixels in size   
def draw(canvas):
    global deck
    # draw cards or blanks
    for i in range(2 * n):
        if exposed[i]:
            canvas.draw_text(str(deck[i]), (10 + 50 * i , 70), font_size, "White")
        else: canvas.draw_polygon([(50 *i, 0), (50 * (i+1), 0), (50 * (i + 1), 100), (50 * i, 100)], 3, "Brown", "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", frame_width, frame_height)
frame.add_button("Restart", init)
moves_label = frame.add_label("Number of moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()