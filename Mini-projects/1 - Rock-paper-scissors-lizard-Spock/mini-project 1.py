# Rock-paper-scissors-lizard-Spock template
# http://www.codeskulptor.org/#user10_YnAubWLX7c6fBop_0.py

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    """
    A function that changes a number between 0 and 4
    to either rock, Spock, paper, lizard or scissors
    """
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Error: an integer value either 0, 1, 2, 3, or 4 is required"
        return
    
def name_to_number(name):
    """
    Takes either rock, Spock, paper, lizard or scissors
    and converts them to an integer between 0 and 4
    """
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print "Error: You did not enter either rock, spock, paper, lizard or scissors"
        return 


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    #print "player_number", player_number
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    #print "comp_no", comp_number
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5

    # print results    
    print "Player chooses", name
    
    # convert comp_number to name using number_to_name
    print "Computer chooses", number_to_name(comp_number)

    
    # use if/elif/else to determine winner
    if difference == 1 or difference == 2:
        print "Player wins!"
        print
         
    elif difference == 3 or difference == 4:
        print "Computer wins!"
        print
    
    else:	         
        print "Player and computer tie!"
        print
        
    
    

    
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


