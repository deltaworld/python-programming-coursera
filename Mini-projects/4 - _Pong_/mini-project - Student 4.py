# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user13_4D9eyP9vjK_42.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [0,0]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0


#    function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    
    if right == True:
       
        ball_vel[0] = random.randrange(120,240)/60
        ball_vel[1] = -random.randrange(60,180)/60
    else:
        ball_vel[0] = -random.randrange(120,140)/60
        ball_vel[1] = -random.randrange(60,180)/60
        
    ball_pos[0] = ball_pos[0]+ball_vel[0]
    ball_pos[1] = ball_pos[1]+ball_vel[1]
    


# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    
    
    ball_init(True)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel > HALF_PAD_HEIGHT )and (paddle1_pos + paddle1_vel <HEIGHT -HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
        
    if (paddle2_pos + paddle2_vel > HALF_PAD_HEIGHT )and (paddle2_pos + paddle2_vel <HEIGHT -HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel  
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
     
    # draw paddles
    paddle1_points = [(0, paddle1_pos- HALF_PAD_HEIGHT), (PAD_WIDTH,paddle1_pos- HALF_PAD_HEIGHT),
                      (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), (0,paddle1_pos+HALF_PAD_HEIGHT)]
    
    paddle2_points = [(WIDTH-PAD_WIDTH, paddle2_pos- HALF_PAD_HEIGHT), (WIDTH,paddle2_pos- HALF_PAD_HEIGHT),
                      (WIDTH, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT)]
    c.draw_polygon(paddle1_points, 1, "YELLOW", "YELLOW")
    c.draw_polygon(paddle2_points, 1, "RED", "RED")
    
    
    # update ball
   
    if (ball_pos[1] <= BALL_RADIUS ) or (ball_pos[1]+ BALL_RADIUS )>= HEIGHT  :
        
        ball_vel [1] = - ball_vel[1]
    
    
    # test ball hit  gutter
    if (ball_pos[0]- BALL_RADIUS) <= PAD_WIDTH: #if touch left gutter, check if touch pad
        if (ball_pos[1] - BALL_RADIUS <= paddle1_pos + HALF_PAD_HEIGHT) and (ball_pos[1]+ BALL_RADIUS >=paddle1_pos -HALF_PAD_HEIGHT ):
            ball_vel [0] = - ball_vel[0]
            ball_vel[1] =  ball_vel[1] + ball_vel[1] *0.1
                                
            
        else: # not touch pad
            ball_pos = [300, 200]
            score2 += 1   
            ball_init(True)
        
            
     
    elif ((ball_pos[0]+BALL_RADIUS )>= WIDTH-PAD_WIDTH):# touch the gutter
        if (ball_pos[1]  + BALL_RADIUS  >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1]-BALL_RADIUS <= paddle2_pos +HALF_PAD_HEIGHT ):
            ball_vel [0] = - ball_vel[0]
            ball_vel[1] =  ball_vel[1] + ball_vel[1] *0.1
           
            
          
        else: # NOT TOUCH PAD
            
            score1 += 1
            ball_pos = [300, 200]
            ball_init(False)
            
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
        
                                                 
                                                    
        
   
    
    # draw ball and scores
    
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    c.draw_text(str(score1), [250,50],40,"YELLOW")
    c.draw_text(str(score2), [350,50],40,"RED")
   
    
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5  
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 5  
     
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= 5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel += 5   
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= 5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel += 5 
    


def button_handler():
    global ball_pos, ball_vel
    ball_pos = [300, 200]
    ball_vel = [0,0]
    new_game()
    
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button = frame.add_button("Restart", button_handler)


# start frame
frame.start()

new_game()


