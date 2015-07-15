# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user13_uIA2eQHm0ijxdt2.py

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

ball_pos = []
ball_vel = []
paddle1_pos = []
paddle2_pos = []
score1 = 0
score2 = 0

# helper function ,that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    x_dir = random.randrange(120,240)
    y_dir = random.randrange(60,180)
    if (right):
        ball_vel = [x_dir/60,-y_dir/60]
    else:
        ball_vel = [-x_dir/60,-y_dir/60]

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    
    score1 = 0
    score2 = 0
    
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0
    
    #Initialize the first ball randonmly
    direction = random.randrange(0,2)
    ball_init(direction)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    
    
    paddle1_pos[1] += paddle1_vel
    if paddle1_pos[1] <= 0 + HALF_PAD_HEIGHT:
        paddle1_pos[1] = 0 + HALF_PAD_HEIGHT
        
    if paddle1_pos[1] >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        
        
    paddle2_pos[1] += paddle2_vel 
    if paddle2_pos[1] <= 0 + HALF_PAD_HEIGHT:
        paddle2_pos[1] = 0 + HALF_PAD_HEIGHT
        
    if paddle2_pos[1] >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT

    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    point1 = [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT]
    point2 = [point1[0] + PAD_WIDTH, point1[1]]
    point3 = [point2[0], point2[1] + PAD_HEIGHT]
    point4 = [point3[0] - PAD_WIDTH, point3[1]]
    paddle = [point1, point2, point3, point4]
    c.draw_polygon(paddle, 1, "White", "White")
    
    point1 = [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT]
    point2 = [point1[0] + PAD_WIDTH, point1[1]]
    point3 = [point2[0], point2[1] + PAD_HEIGHT]
    point4 = [point3[0] - PAD_WIDTH, point3[1]]
    paddle = [point1, point2, point3, point4]
    c.draw_polygon(paddle, 1, "White", "White")
    
    
    # update ball
    check_colission()
    
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
        
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    c.draw_text("PLAYER1", [WIDTH/2 - 150, 75], 20, "White")
    c.draw_text(str(score1), [WIDTH/2-115, 105], 20, "White")
    
    c.draw_text("PLAYER2", [WIDTH/2 + 95, 75], 20, "White")
    c.draw_text(str(score2), [WIDTH/2 + 115, 105], 20, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP['s']):
        paddle1_vel = 3
        
    if (key == simplegui.KEY_MAP['w']):
        paddle1_vel = -3
        
        
    if (key == simplegui.KEY_MAP['up']):
        paddle2_vel = -3
        
    if (key == simplegui.KEY_MAP['down']):
        paddle2_vel = 3
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP['s']):
        paddle1_vel = 0
        
    if (key == simplegui.KEY_MAP['w']):
        paddle1_vel = 0
        
        
    if (key == simplegui.KEY_MAP['up']):
        paddle2_vel = 0
        
    if (key == simplegui.KEY_MAP['down']):
        paddle2_vel = 0

#Check a colission against wall or paddle/gutter
def check_colission():
    global ball_vel
    global score1, score2
   
    
    #Colission against top
    if (ball_pos[1] - BALL_RADIUS <= 0):
        ball_vel[1] = -ball_vel[1]
        
        
    #Colission against bot
    if (ball_pos[1] + BALL_RADIUS >= HEIGHT):
        ball_vel[1] = -ball_vel[1]
        
    #Colission against right gutter
    if (ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH):
        if ((ball_pos[1] >= (paddle2_pos[1]-HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle2_pos[1] + HALF_PAD_HEIGHT))):
            ball_vel[0] = -1.1*ball_vel[0]
            ball_vel[1] *= 1.1
        else:
            ball_init(0)
            score1 += 1
        
    #Colission against left gutter
    if (ball_pos[0] - BALL_RADIUS <= 0 + PAD_WIDTH):
        if ((ball_pos[1] >= (paddle1_pos[1]-HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle1_pos[1] + HALF_PAD_HEIGHT))):
            ball_vel[0] = -1.1*ball_vel[0]
            ball_vel[1] *= 1.1
        else:
            ball_init(1)
            score2 += 1
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()
frame.add_button("Reset", new_game)

new_game()
