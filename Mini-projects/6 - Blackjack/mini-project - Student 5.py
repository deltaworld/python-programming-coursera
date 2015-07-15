# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user15_gMy8TamWoX_5.py

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
draw_card_face_down = False
outcome = ""
player_message = ""
dealer_message = ""
dealer_name = ""
player_name = ""
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
        self.hand = []    

    def __str__(self):
        ans = ""
        for i in range(len(self.hand)):
            ans += " " + str(self.hand[i])
        return "Hand contains"	+ ans    # return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        ace_count = 0
        hand_value = 0
        for i in range(len(self.hand)):
            if self.hand[i].get_rank() == 'A':
                ace_count += 1
                hand_value += VALUES[self.hand[i].get_rank()]
            else:
                hand_value += VALUES[self.hand[i].get_rank()]
        if ace_count > 0:
            if hand_value + 10 <= 21:
                hand_value += 10
        return hand_value
    
    def draw(self, canvas, pos):    # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, pos)
            pos[0] += 75
        

# define deck class 
class Deck:  
    def __init__(self):  # create a Deck object
        self.deck_lst = []
        for s in SUITS:
            for r in RANKS:
                self.deck_lst.append(str(Card(s,r)))
        random.shuffle(self.deck_lst)        
        
    def shuffle(self):    # add cards back to deck and shuffle
        for s in SUITS:
            for r in RANKS:
                self.deck_lst.append(str(Card(s,r)))
        random.shuffle(self.deck_lst)   
        
    def deal_card(self):    # deal a card object from the deck
        a = ""
        a = self.deck_lst.pop()
        return Card(a[0], a[1])
    
    def __str__(self):
        ans = " ".join(self.deck_lst)
        
        return "Deck contains " + str(len(self.deck_lst)) + " cards: " + ans 	# return a string representing the deck

#define event handlers for buttons
def deal():
    global outcome, in_play, draw_card_face_down, player_hand, dealer_hand, game_deck
    global player_message, dealer_message, dealer_name, player_name, score
    
    #  asign variable used in the draw handler
    dealer_name, player_name = "Dealer's hand", "Player's hand    hit or stand?"
    
    #  as the card deck gets low, another deck of cards are added and shuffled
    if int(str(game_deck)[13:16]) <= 10:
        game_deck.shuffle()
    
    if outcome != "":
        outcome = ""
        player_message = ""
        dealer_message = ""
        
    #  this records a loss if the 'deal button' is pressed during a round
    if in_play:
        score -= 1
        
    #  creates a 'Hand' object for both player and dealer and deals two cards each
    dealer_hand = Hand()
    player_hand = Hand()
    player_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    player_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
        
    draw_card_face_down = True
    in_play = True

def hit():  # if the hand is in play, hit the player
    
    global outcome, draw_card_face_down, score, player_message, in_play, player_name
    if in_play:
        player_hand.add_card(game_deck.deal_card())
        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "Dealer wins!"
            player_message = "Player Busted"
            player_name = "Player's hand       new deal?"
            score -= 1
            draw_card_face_down = False  # turns over the dealer's hole card
            in_play = False
           
def stand():
    
    global draw_card_face_down, outcome, score, player_message, dealer_message, in_play, player_name
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(game_deck.deal_card())
        
    draw_card_face_down = False  # turns over the dealer's hole card
    
    # assign a message to outcome and update score
    if in_play:
        if dealer_hand.get_value() > 21:
            outcome = "Player wins!"
            dealer_message = "Dealer Busted"
            player_name = "Player's hand       new deal?"
            score += 1
        elif dealer_hand.get_value() >= player_hand.get_value():
            outcome = "Dealer wins!"
            dealer_message = "Dealer has " + str(dealer_hand.get_value())
            player_message = "Player has " + str(player_hand.get_value())
            player_name = "Player's hand       new deal?"
            score -= 1
        else:
            outcome = "Player wins!"
            dealer_message = "Dealer has " + str(dealer_hand.get_value())
            player_message = "Player has " + str(player_hand.get_value())
            player_name = "Player's hand       new deal?"
            score += 1
    
    in_play = False  # update in_play

   
def draw(canvas):  # draw handler 
    if in_play or outcome != "":
        dealer_hand.draw(canvas, [50, 230])
        player_hand.draw(canvas, [50, 450])
        
        if draw_card_face_down:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_CENTER[0], 230 + CARD_CENTER[1]], CARD_SIZE)
            
    canvas.draw_text("Blackjack", (150, 60), 75, "Black")
    canvas.draw_text("Score: " + str(score), (400, 220), 36, "Blue")    
    canvas.draw_text(dealer_message, (50, 360), 36, "Blue")
    canvas.draw_text(player_message, (50, 580), 36, "Blue")
    canvas.draw_text(dealer_name, (25, 220), 48, "Cyan")
    canvas.draw_text(player_name, (25, 438), 48, "Cyan")
    canvas.draw_text(outcome, (275, 140), 60, "Yellow")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

game_deck = Deck()
print game_deck

# get things rolling
frame.start()

deal()