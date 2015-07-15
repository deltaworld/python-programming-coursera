# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user15_hHGPKVvAYS_0.py

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
        #pass	# create Hand object
        self.cards = []
        
    def __str__(self):
        #pass	# return a string representation of a hand
        ret = ''
        for card in self.cards:
            ret += ' ' + str(card)
        return "Hand contains " + ret
        
    def add_card(self, card):
        #pass	# add a card object to a hand
        self.cards.append(card)
    
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        #pass	# compute the value of the hand, see Blackjack video
        has_ace = False
        hand_value = 0
        for card in self.cards:
            if card.get_rank() == 'A':
                has_ace = True
            hand_value += VALUES[card.get_rank()]
        if has_ace:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
        else:
            return hand_value

    def draw(self, canvas, pos):
        #pass	# draw a hand on the canvas, use the draw method for cards
        n = 1
        for card in self.cards:
            card.draw(canvas, [(pos[0] + 10) * n, pos[1]])
            n += 1

        
# define deck class 
class Deck:
    def __init__(self):
        #pass	# create a Deck object
        self.cards = []
        self.deal_cards = []
        for suit in SUITS:
            for rank in RANKS:
                c = Card(suit, rank)
                self.cards.append(c)
        self.shuffle()
        
    def shuffle(self):
        # add cards back to deck and shuffle
        #pass	# use random.shuffle() to shuffle the deck
        self.cards += self.deal_cards
        self.deal_cards = []
        random.shuffle(self.cards)
    
    def deal_card(self):
        #pass	# deal a card object from the deck
        c = self.cards.pop()
        self.deal_cards.append(c)
        return c
    
    def __str__(self):
        #pass	# return a string representing the deck
        ret = "Deck contains "
        for card in self.cards:
            ret += " " + str(card)
        return ret


deck = None
dealer_hand = None
player_hand = None
#define event handlers for buttons
def deal():
    global outcome, in_play, score
    global deck, dealer_hand, player_hand
    # your code goes here
    
    if in_play:    
        score -= 1
    else:
        in_play = True
    
    deck = Deck()
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())    
    dealer_hand.add_card(deck.deal_card())
    
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())    
    player_hand.add_card(deck.deal_card())

    


def hit():
    global in_play, score, outcome
    # if the hand is in play, hit the player

    if in_play:
        if player_hand.get_value() <= 21:
            card = deck.deal_card()
            player_hand.add_card(card)
        
    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21:
        outcome = "You went bust and lose."
        win = -1
        if in_play:
            score += win
            in_play = False
        
 
def stand():
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global in_play
    global score
    global outcome
    if in_play:
        if player_hand.get_value() > 21:
            outcome = "You have busted"
            win = -1
        else:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal_card())
            
            if player_hand.get_value() <= dealer_hand.get_value() < 21:
                outcome = "You lose."
                win = -1
            else:
                outcome = "You win."
                win = 1
        score += win
    
    # assign a message to outcome, update in_play and score
    in_play = False


# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    
    # title
    canvas.draw_text("Blackjack", (100, 100), 36, "Aqua")
    
    # score
    canvas.draw_text("Score " + str(score), (400, 100), 24, "Black")

    # dealer
    canvas.draw_text("Dealer", (80, 180), 24, "Black")
    
    if dealer_hand:
        pos = [CARD_SIZE[0], CARD_SIZE[1] * 2]
        dealer_hand.draw(canvas, pos)
        
        if in_play:
            pos = [CARD_SIZE[0] + 10, CARD_SIZE[1] * 2]
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_BACK_SIZE)

    # player    
    canvas.draw_text("Player", (80, 380), 24, "Black")
    
    if not in_play:
        canvas.draw_text(outcome, (250, 190), 24, "Black")
    
    # prompt
    if in_play:
        prompt = "Hit or Stand?"
    else:
        prompt = "New deal?"
    canvas.draw_text(prompt, (250, 380), 24, "Black")

    if player_hand:
        pos = [CARD_SIZE[0], CARD_SIZE[1] * 4]
        player_hand.draw(canvas, pos)

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
deal()

# remember to review the gradic rubric