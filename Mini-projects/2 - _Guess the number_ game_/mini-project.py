# http://www.codeskulptor.org/#user11_mt9xM0tXbHDaDHF_4.py
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

# initialize global variables used in your code
secret_number = 0
numrange = 100
guesses = 0


def init():
    """ Initializer function for either range """
    global secret_number, numrange, guesses
    secret_number = random.randrange(0, numrange)
    print "New game, Range is from 0 to", numrange
    print "Number of guesses remaining is", guesses
    print ""

def message(guess):
    """ 
    Prints out depending remaining guesses the guess value
    and if you ran out of guesses. This also restarts the game
    if you ran out of guesses.
    """
    global guesses
    guesses -= 1
    if guesses > 0:
        print "Guess was", guess
        print "Number of guesses remaining is", guesses
    else:
        print "You ran out of guesses. The number was", secret_number
        print ""
        if numrange == 100:
            range100()
        else:
            range1000()


def guesses_calculation():
    """
    Calculation of the optimum number of guesses needed
    depending on the range given
    """
    global guesses
    guesses = math.ceil(math.log(numrange - 0 + 1, 2))

# define event handlers for control panel
# button that changes range to range [0,100) and restarts
def range100():
    """Resets range to 100 and works out guess calc"""
    global numrange
    numrange = 100
    guesses_calculation()
    init()
    
# button that changes range to range [0,1000) and restarts
def range1000():
    """Resets range to 1000 and guess_calc and init"""
    global numrange, guesses
    numrange = 1000
    guesses_calculation()
    init()
     
    
def get_input(guess):
    """
    Handler for gathering the data entered. Prints out
    hints depending on the value of the number
    """
    global guesses
    # main game logic goes here	
    guess = int(guess)
    if guess == secret_number:
        print "Well Done you got it", guess
        print ""
    else:
        message(guess)
        if guess < secret_number:
            print "Higher"
            print ""
        else:
            print "Lower"
            print ""      
           
#create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements
frame.add_button("Range 0 - 99", range100, 100)
frame.add_button("Range 0 - 999", range1000, 100)
frame.add_input("Input Number", get_input, 100)

#starts the game
range100()

# start frame
frame.start()

# always remember to check your completed program against the grading rubric
