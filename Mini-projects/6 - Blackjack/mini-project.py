# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user15_ijPyCSqCqCplzcF_7.py

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
outcome = "New Deal?"
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
        self.cards = []
        # create Hand object

    def __str__(self):
        msg = "Hand contains "
        cards = ""
        if len(self.cards) > 0:
            for c in self.cards:
                cards += c.get_suit()
                cards += c.get_rank()
                cards += " "
                #return msg + str(c)
        return msg + cards
            
    def add_card(self, card):
        self.cards.append(card)
        pass	# add a card object to a hand

    def get_value(self):
        ranks = []
        hand_value = 0
        
        for c in self.cards:
            rank = c.get_rank()
            ranks.append(VALUES[rank])
        
        for i in ranks:
                hand_value += i
        if ranks.count(1) == 0:
            """Hand has no Aces"""
            return hand_value
        else:
            if (hand_value + 10) <= 21:
                return hand_value + 10
            else:
                return hand_value
      
            
            
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        #pos = [100, 100]
        i = 0
        for c in self.cards:
            i += 1
            pos[0] = i * (CARD_SIZE[0]+5)
            c.draw(canvas, pos) 
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                card = Card(s, r)
                self.deck.append(card)
            # create a Deck object

    def shuffle(self):
        Deck()
        random.shuffle(self.deck)
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck

    def deal_card(self):
        return self.deck.pop()
        # deal a card object from the deck
    
    def __str__(self):
        deck = ""
        for c in self.deck:
            deck +=str(c)
            deck += " "
        return deck
        # return a string representing the deck

deck = Deck()
dealer = None
player = None


#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, score, deck
    deck = Deck()
    if in_play == True:
        outcome = "You lose this round"
        score -= 1
        in_play = False
    
    else :
        outcome = "Hit or Stand?"
    # your code goes here
        deck.shuffle()
        
        # creates 2 hands 1 for the dealer and the other for the player
        dealer = Hand()
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
       
        player = Hand()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
    
        print "Dealers", dealer, dealer.get_value()
        
        print "Players", player, player.get_value()
        
        in_play = True

def hit():
    global outcome, in_play, score
    # if the hand is in play, hit the player
    if player.get_value() <= 21:
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            outcome = "You have busted"
            score -= 1
            in_play = False
        print player.get_value()
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, score
    if player.get_value() > 21:
        outcome = "You have busted"
        score -= 1
        in_play = False
    else:
        """Hit the dealer till he has 17 or more"""
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "You win, Dealer Busted"
            score += 1
            in_play = False
        else:
            in_play = False
            if dealer.get_value() >= player.get_value():
                outcome = "Dealer wins"
                score -= 1
            else:
                outcome = "You win!!"
                score += 1
            
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    if dealer == None:
        pass
    else:
        canvas.draw_text("Dealer", (80, 90), 36, "Black")
        dealer.draw(canvas, [100, 100])
        canvas.draw_text("Player", (80, 290), 36, "Black")
        player.draw(canvas, [200, 300])
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, 
                      CARD_BACK_SIZE, [112, 150], CARD_SIZE)
        
    canvas.draw_text(outcome, (50, 50), 36, "White")
    canvas.draw_text("Score: " + str(score), (450, 50), 20, "Brown")
    canvas.draw_text("Blackjack", (50, 580), 50, "Black")
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    

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


# remember to review the gradic rubric