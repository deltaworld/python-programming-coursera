# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user13_EGIgcH3rBErzS95_2.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
# CONSTANTS
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
PADDLE_VEL = 3

# global variables
ball_pos = 0
ball_vel = 0

paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT

# test paddle position
#paddle1_pos = 0
#paddle2_pos = 43

#paddle1_vel = -1
#paddle2_vel = 1

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0
# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
        
    # horizontal & vertical random velocity pixels per second
    h_vel = random.randrange(120, 240) / 60
    v_vel = random.randrange(60, 180) / 60
    
    ball_vel = [h_vel, v_vel]
    
    # randomisation to velocity
    # True == up, right || False = up, left
    if right == False:
        ball_vel[0] = -ball_vel[0]
def vel_inc_bounce():
    ball_vel[0] *= 1.1
    ball_vel[1] *= 1.1
    ball_vel[0] = -ball_vel[0]
        
# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    ball_init(True)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # 7. draw paddles
    # PADDLEs
    pad1_b = paddle1_pos + PAD_HEIGHT
    pad2_b = paddle2_pos + PAD_HEIGHT
    pad2_l = WIDTH - PAD_WIDTH
    
    # 8 paddle position affected by vel
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # 10 check position of paddles
    if paddle1_pos < 0:
        paddle1_pos = 0
    elif paddle1_pos > HEIGHT - PAD_HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT
    
    if paddle2_pos < 0:
        paddle2_pos = 0
    elif paddle2_pos > HEIGHT - PAD_HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT
    
    c.draw_polygon([(0, paddle1_pos), (0, pad1_b), (PAD_WIDTH, pad1_b), (PAD_WIDTH, paddle1_pos)], 1, "White", "White")
    c.draw_polygon([(pad2_l, paddle2_pos), (pad2_l, pad2_b), (WIDTH, pad2_b), (WIDTH, paddle2_pos)], 1, "White", "White")

    
    # update ball
    # ball movement
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # bounce off top and bottom walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT-BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # 6. left & right gutter
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        # left gutter
        if paddle1_pos < ball_pos[1] and ball_pos[1] < paddle1_pos + PAD_HEIGHT:
            vel_inc_bounce()
        else:
            score2 += 1
            ball_init(True)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        # right gutter
        if paddle2_pos < ball_pos[1] and ball_pos[1] < paddle2_pos + PAD_HEIGHT:
            vel_inc_bounce()
        else:
            score1 += 1
            ball_init(False)
    
    # draw ball and scores
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "white", "white")
    
    # Scores
    
    c.draw_text(str(score1), (210, 50), 50, "White", "monospace")
    c.draw_text(str(score2), (350, 50), 50, "White", "monospace")

    
# 9. w = up, s = down for paddle1, up = up, down = down for paddle 2    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -PADDLE_VEL
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = PADDLE_VEL
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -PADDLE_VEL
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = PADDLE_VEL
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)


# start frame
frame.start()
new_game()
