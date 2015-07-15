# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user15_bAf3GUFYVv_13.py

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cardlist = []	# create Hand object

    def __str__(self):
        s = ""
        for i in self.cardlist:
            s += i.suit + i.rank + " "
        return s	# return a string representation of a hand

    def add_card(self, card):
        self.cardlist.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        handvalue = 0 # compute the value of the hand, see Blackjack video
        acepresent = 0
        for i in self.cardlist:
            handvalue += VALUES[i.rank]
            if i.rank == 'A': acepresent = 1          
        if handvalue <= 11 and acepresent == 1: handvalue += 10
        return handvalue
   
    def draw(self, canvas, pos):
        x = 0
        for i in self.cardlist:
            i.draw(canvas, [pos[0] + x, pos[1]])	# draw a hand on the canvas, use the draw method for cards
            x += CARD_SIZE[0]
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(x,y) for x in SUITS for y in RANKS]	# create a Deck object
        
        
    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.deck)	# use random.shuffle() to shuffle the deck

    def deal_card(self):
        x = len(self.deck)
        return self.deck[random.randrange(0,x)]	# deal a card object from the deck
    
    def __str__(self):
        s = ""
        for i in self.deck:
            s += i.suit + i.rank + " "
        return s	# return a string representing the deck


    
    
    

#define event handlers for buttons
def deal():
    global outcome, in_play, score, player_hand, dealer_hand, mydeck

    mydeck = Deck()
    mydeck.shuffle()
    #print str(mydeck)
    player_hand = Hand()
    dealer_hand = Hand()
    outcome = "Hit or Stand?"
    
    if in_play: score -= 1
       
    player_hand.add_card(mydeck.deal_card())
    dealer_hand.add_card(mydeck.deal_card())
    player_hand.add_card(mydeck.deal_card())
    dealer_hand.add_card(mydeck.deal_card())
    
    #print "Dealer hand: ", str(dealer_hand), ", Player Hand", str(player_hand)
    #print "Dealer hand value: ", dealer_hand.get_value(), ", Player Hand value", player_hand.get_value()
    
    in_play = True

def hit():
    global outcome, in_play, score
    
    if player_hand.get_value() <= 21 and in_play: 
        player_hand.add_card(mydeck.deal_card())
            
    #print "Dealer hand: ", str(dealer_hand), ", Player Hand", str(player_hand)
    #print "Dealer hand value: ", dealer_hand.get_value(), ", Player Hand value", player_hand.get_value()
    if player_hand.get_value() >21 and in_play: 
        outcome = "You Have Busted!"
        score -= 1
        in_play = False
    
    
def stand():
    global outcome, in_play, score
    
    if player_hand.get_value() > 21: 
        outcome = "You Have Busted!"
        in_play = False
        return
    
    while (dealer_hand.get_value() < 17):
        dealer_hand.add_card(mydeck.deal_card())
        #print "Dealer hand: ", str(dealer_hand), ", Player Hand", str(player_hand)
        #print "Dealer hand value: ", dealer_hand.get_value(), ", Player Hand value", player_hand.get_value()
    
    if dealer_hand.get_value() > 21 and in_play: 
        outcome = "Dealer Busted!, You WIN!! ;)"
        score += 1
        in_play = False
    elif dealer_hand.get_value() >= player_hand.get_value() and in_play:
            outcome = "Dealer won by a horse's nose!"
            score -= 1
            in_play = False
    elif in_play:
        outcome = "YOU WON!!!"
        score += 1
        in_play = False
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

    
    
    
# draw handler    
def draw(canvas):
    global outcome, CARD_BACK_SIZE, CARD_BACK_CENTER, in_play
    # test to make sure that card.draw works, replace with your code below
        
    player_hand.draw(canvas, [150, 350])
    dealer_hand.draw(canvas, [50, 100])
    canvas.draw_text(outcome,[150,50], 29, "orange", "serif")
    canvas.draw_text("Score: " + str(score),[10,80], 29, "black", "serif")
    canvas.draw_text('Blackjack!',[10,50], 29, "black", "serif")
    if in_play: canvas.draw_image(card_back, (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1]), CARD_BACK_SIZE, [50 + 36.5, 100 + 49], CARD_BACK_SIZE)
                     
    
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()

player_hand = Hand()
dealer_hand = Hand()
mydeck = Deck()
outcome = "Deal?"

# remember to review the gradic rubric