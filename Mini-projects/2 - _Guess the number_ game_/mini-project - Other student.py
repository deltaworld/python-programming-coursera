# Mini-Project: Guess The Number (Week 2)
# http://www.codeskulptor.org/#user11_68jvM1sVG3_13.py
# Score: 11
# 
import simplegui

import random
#


player_guess    = 0
comptr_nbr      = 0
##
num_range       = 100
nbr_guesses_allowed = 7
nbr_remaining_guesses = 7
#########################################################

#########2
#########2
#  Helper Function to initialize game variables
def init(): pass

def determine_last_chance():
    global nbr_remaining_guesses
    if comptr_nbr == player_guess:
        
        print "You Guessed Correct"
        print "New game. Range is from 0 to ", num_range
        print " "
        nbr_remaining_guesses = nbr_guesses_allowed
    else:
        
        print "Number of remaining guesses is 0 "
        print "You ran out of guesses. The number was", comptr_nbr 
        print " "
        print "New game. Range is from 0 to ", num_range
        nbr_remaining_guesses = nbr_guesses_allowed
        print "Number of remaining guesses is ", nbr_remaining_guesses
        print " "  
        


#   Helper function to determine winner
def determine_game_status():
    global nbr_remaining_guesses
    if comptr_nbr == player_guess:
                
        print "You Guessed Correct"
        print "New game. Range is from 0 to ", num_range
        nbr_remaining_guesses = nbr_guesses_allowed
        print "Number of remaining guesses is ", nbr_remaining_guesses
        print " "
    elif comptr_nbr > player_guess:
                
        print "Guess was ", player_guess
        print "Number of remaining guesses is ", nbr_remaining_guesses
        print "Higher!"
        print " "
    else: 
        
        print "Guess was ", player_guess
        print "Number of remaining guesses is ", nbr_remaining_guesses
        print "Lower!"
        print " "
        
    
    
    
#########4
#########4
# Handler for Range 100
def range100():
    
    global num_range
    global nbr_guesses_allowed
    global nbr_remaining_guesses
    num_range = 100
    nbr_guesses_allowed   = 7
    nbr_remaining_guesses = 7   
    
    
# Handler for Range 1000
def range1000():
    
    global num_range
    global nbr_guesses_allowed
    global nbr_remaining_guesses
    num_range = 1000
    nbr_guesses_allowed   = 10
    nbr_remaining_guesses = 10
#
    
  
##   Main program logic    
def get_input(guess):
    
    global player_guess
    global nbr_remaining_guesses
    global comptr_nbr
    if nbr_remaining_guesses == nbr_guesses_allowed:
        comptr_nbr = random.randrange(0,num_range)
        
    nbr_remaining_guesses = nbr_remaining_guesses - 1
    player_guess = float(guess)
    
    
    
    if nbr_remaining_guesses == 0:
        
        determine_last_chance()
    else:
        
        determine_game_status()
############################END OF HANDLERS    #########

##############5
##############5   CREATE FRAME
# Create a frame 
f = simplegui.create_frame("Guess a Number", 300, 200)

##############6 REGISTER EVENT HANDLERS
# register event handlers and create control elements
f.add_button("Range is (0,100) ", range100,  200)
f.add_button("Range is (0,1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 100)

################7  START FRAME
f.start()
    
