# http://www.codeskulptor.org/#user14_yHibIewR4M_69.py
# implementation of card game - Memory
# Rev - 7

import simplegui
import random


# global variables
x = 0
face = []
border = []
card_pos = []
font_pos = []
num = []
open_cards = 0
font_size = 60
i = 55
listd = []
listi = []
list3 = []
click = 0
clicks = []
cards2 = []
matched = []
moves = []
m = len(moves)
#moves_txt = len(moves)
#moves_txt = 3

def init():
    global face,border,card,card_pos,font_size,font_pos,x,num,matched, moves, moves_txt,m,clicks,listd,listi
# initializing variables
    x = 0
    face = []
    border = []
    card_pos = []
    font_pos = []
    num = []
    open_cards = 0
    font_size = 60
    i = 55
    listd = []
    listi = []
    list3 = []
    click = 0
    clicks = []
    cards2 = []
    matched = []
    moves = []
    m = len(moves)
    label.set_text("Moves = 0")
    #moves_txt = len(moves)
    #moves_txt = 5

    for k in range(16):
     face.append("Green")
     border.append("White")
     card = ( [0+x,0], [50+x,0], [50+x,100], [0+x,100] )
     card_pos.append(card)
     font = (10+x,65)
     font_pos.append(font)
     x+=50
    num = ["0", "1", "2","3","4","5","6","7","0", "1", "2", "3","4","5","6","7"]
    random.shuffle(num)
    matched = []
    print "SHUFFLE",num
    
    #print face[15]
    #print border[15]
    #print card_pos[15]
    #print font_pos

# helper function to initialize globals
#def init():
 #   pass  

     
# define event handlers
def mouseclick(pos):
    global cards, face, border, i, num, clicks, click,listd, listi, list3,matched,moves,moves_txt,m
  # add game state logic here
    
    x=0
    for k in range(16):
        if 0+x<pos[0]<50+x:
         i = k
        x+=50
    print "This is i: ", i
    if not i in clicks:
        face[i] = "Black"
        clicks.append(i)
        listd.append(num[i])
        listi.append(i)
        moves.append(i)
        #m = len(moves)
        #label.set_text("Moves = " + str(m))
        print "Moves: ",moves
        #moves_txt = len(moves)
        #print "MOVES-TExT: ", moves_txt
    else:
       pass
        
    print "Clicks: ",clicks
   
    if len(clicks) <= 2:    
        face[i] = "Black"
        #listd.append(num[i])
        #listi.append(i)
        print "ListeD: ",listd
        #print listi
        #print "click1: ",click
    
    elif str(listd[0]) == str(listd[1]):
        face[i] = "Black"
        matched += listi
        listd = []
        listi = []
        clicks = []
        print "MATCHED: ",matched
        print "ListD Clear: ",listd
        listd.append(num[i])
        listi.append(i)
        clicks.append(i)
        #print "click2: ", click
        print "ListD 2nd: ",listd
    
    else:
        face[i] = "Black"
        listi.pop()
        for n in listi:
            face[n] = "Green"
        listd = []
        listi = []
        clicks = []
        print "ListD Clear-Else",listd
        listd.append(num[i])
        listi.append(i)
        clicks.append(i)
        print "ListD added-Else", listd
        print "Clicks in Else: ",clicks
        #click = 1
        #print "click3: ", click
    for i in matched:
        face[i] = "Black"
    
    #m = len(moves)
    print "MMM",m
    #x = 1
    #if len(moves) == 1 or len(moves) == 2:
        #moves_txt = len(moves)
        #print "MOVES-TEST: ", moves_txt
        #x+=1
    m = len(moves)
    if 1<=m<= 2:
        m = 1
    if 3<=m<= 4:
        m = 2
    if 5<=m<= 6:
        m = 3
    if 7<=m<= 8:
        m = 4
    if 9<=m<= 10:
        m = 5
    if 11<=m<= 12:
        m = 6
    if 13<=m<= 14:
        m = 7
    if 15<=m<= 16:
        m = 8
    if 17<=m<= 18:
        m = 9
    if 19<=m<= 20:
        m = 10
    if 21<=m<= 22:
        m = 11        
    if 23<=m<= 24:
        m = 12
    if 25<=m<= 26:
        m = 13        
    if 27<=m<= 28:
        m = 14        
    if 29<=m<= 30:
        m = 15
    if 31<=m<= 32:
        m = 16
        
        
    label.set_text("Moves = " + str(m))

    
    
              
# cards are logically 50x100 pixels in size  

def draw(canvas):
    global card_pos,border,face,num,font_pos,font_size
    j=0
    while j<16:
     canvas.draw_polygon( card_pos[j], 1, border[j], face[j])
     canvas.draw_text(num[j], font_pos[j], font_size, "Green")
     j+=1


print "MMM-2",m
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
#print "MOVESTEXT",moves_txt

label = frame.add_label("Moves = 0")
#label.set_text("Moves = "+str(m)

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric