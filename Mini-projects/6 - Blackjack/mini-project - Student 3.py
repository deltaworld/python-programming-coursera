# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user15_TRUipaQtHI_7.py

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
        self.list_of_hand=list()
        # create Hand object

    def __str__(self):
        result=''
        if len(self.list_of_hand)>0:
            for card in self.list_of_hand:
                result+=str(card)+' '
        return "Hand Contains "+ result
        # return a string representation of a hand

    def add_card(self, card):
        self.list_of_hand.append(card)
        # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value=0
        count_ace=0
        for card in self.list_of_hand:
            hand_value+=VALUES[card.get_rank()]
            if card.get_rank()=='A':
                count_ace+=1
        if count_ace>0:
            if hand_value+10<=21:
                return hand_value+10
            else:
                return hand_value
        else:
            return hand_value
            
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for card in self.list_of_hand:
            card_pos=[pos[0]+CARD_SIZE[0]*self.list_of_hand.index(card),pos[1]]
            card.draw(canvas, card_pos)
        # draw a hand on the canvas, use the draw method for cards
 

    
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_of_cards=[]
        for suit in SUITS:
            for rank in RANKS:
                c=Card(suit, rank)
                self.deck_of_cards.append(c)
        # create a Deck object

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.deck_of_cards)
        # use random.shuffle() to shuffle the deck

    def deal_card(self):
        return self.deck_of_cards.pop()
        # deal a card object from the deck
    
    def __str__(self):
        result=''
        if len(self.deck_of_cards)>0:
            for card in self.deck_of_cards:
                result+=str(card)+' '
        return "Deck Contains "+ result
        # return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score
    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    dealer_hand=Hand()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    #print "Player Hand "+ str(player_hand) + "AND " +"Dealer Hand "+ str(dealer_hand)
    # your code goes here
    outcome='Hit or Stand?'
    if in_play:
        score-=1
        outcome="Aborted midgame, New Game,Hit or Stand"
        print outcome + "Player Hand: "+ str(player_hand.get_value())+ "Dealer Hand: "+ str(dealer_hand.get_value())
    in_play = True

def hit():
    global player_hand, outcome, deck, in_play, score
    # replace with your code below
    if in_play:
        if player_hand.get_value()<=21:
            player_hand.add_card(deck.deal_card())
        else:
            outcome= "You went bust and lost! New deal?"
            score-=1
            in_play=False
            print outcome, "Player Hand: "+ str(player_hand.get_value())
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global player_hand, dealer_hand, outcome, deck, in_play, score
    if in_play:
        if player_hand.get_value()>21:
            outcome= "You went busted and lost! New deal?"
            score-=1
            in_play=False
            print outcome, "Player Hand: "+ str(player_hand.get_value())
        else:
            in_play=False
            while dealer_hand.get_value()<=17:
                dealer_hand.add_card(deck.deal_card())
            if dealer_hand.get_value()>21:
                outcome= "You Win! New Deal?"
                score+=1
            elif dealer_hand.get_value()>=player_hand.get_value():
                outcome= "You Lose! New Deal?"
                score-=1
            else:
                outcome= "You Won! New Deal?"
                score+=1
        print outcome + "Player Hand: "+ str(player_hand.get_value())+ "Dealer Hand: "+ str(dealer_hand.get_value())
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player_hand, dealer_hand, outcome, in_play, score, hand_sums
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    
    #grid lines
    #canvas.draw_line([20, 0], [20, 600], 1, "Blue")
    #canvas.draw_line([0, 100], [600, 100], 1, "Blue")
    canvas.draw_polygon([(0, 0), (600, 0), (600, 100), (0,100)], 1, "#333333", "#333333")
    canvas.draw_polygon([(0, 280), (600, 280), (600, 350), (0,350)], 1, "#333333", "#628B61")
    #canvas.draw_line([0, 60], [600, 60], 1, "#444444")
    #canvas.draw_line([0, 61], [600, 61], 1, "#111111")
    canvas.draw_line([0, 100], [600, 100], 1, "#444444")
    canvas.draw_line([0, 101], [600, 101], 1, "Black")
    canvas.draw_text("Blackjack", (22, 53), 40, "Black")
    canvas.draw_text("Blackjack", (20, 50), 40, "#EEEEEE")
    canvas.draw_text("Score :"+str(score), (20, 85), 24, "#FCD271")
    canvas.draw_text("Dealer", (21, 142), 24, "#102E37", "sans-serif")
    canvas.draw_text("Dealer", (20, 140), 24, "#EEEEEE", "sans-serif")
    canvas.draw_text("You", (21, 392), 24, "#102E37", "sans-serif")
    canvas.draw_text("You", (20, 390), 24, "White", "sans-serif")
    #canvas.draw_text(outcome, (22, 324), 24, "Black", "sans-serif")
    canvas.draw_text(outcome, (20, 320), 24, "White", "sans-serif")
    
    dealer_hand.draw(canvas, [20,150])
    player_hand.draw(canvas, [20,400])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [20 + CARD_BACK_CENTER[0], 150 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("#397249")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
deal()
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric