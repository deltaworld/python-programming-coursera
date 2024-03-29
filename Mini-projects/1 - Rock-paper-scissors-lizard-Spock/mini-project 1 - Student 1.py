# Rock-paper-scissors-lizard-Spock template
# http://www.codeskulptor.org/#user10_8Uu3jtFqIjpR3ty.py

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
import random

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        print "Wrong number passed"

    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if(name == "rock"):
        return 0
    elif(name == "Spock"):
        return 1
    elif(name == "paper"):
        return 2
    elif(name == "lizard"):
        return 3
    elif(name == "scissors"):
        return 4
    else:
        print "Wrong option"

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_option = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    computer_option = random.randrange(0,5)

    # compute difference of player_number and comp_number modulo five
    score = (player_option - computer_option) % 5

    print "Player chooses " + name
    print "Computer chooses " + number_to_name(computer_option)
    
    if(score == 0):
        print "Player and computer tie!\n"
    elif(score <= 2):
        print "Player wins!\n"
    else:
        print "Computer wins!\n"

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


