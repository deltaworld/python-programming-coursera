# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user12_09EFeFQ89j_0.py

import simplegui

# define global variables

ts = 0
interval = 100
message = "0:00.0"
score = 0
attempts = 0
timer_ON = False

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    global message
    minutes = (t-(t%600))/600
    t = t - minutes*600
    seconds = (t-t%10)/10
    t = t - seconds*10
    message  = '%d:%02d.%d' % (minutes,seconds,t)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_btn_handler():
    global timer_ON
    timer.start()
    timer_ON = True

def stop_btn_handler():
    global message
    global score
    global attempts
    global timer_ON
    timer.stop()
    if timer_ON : 
        attempts = attempts + 1
        if int(message[5]) == 0:
            score = score + 1
    timer_ON = False

def reset_btn_handler():
    timer.stop()
    global ts
    global score
    global attempts
    score = 0
    attempts = 0
    ts = 0
    format(ts)

# define event handler for timer with 0.1 sec interval
def tick():
    global ts
    ts=ts+1
    format(ts)

# define handler to draw on canvas

def draw(canvas):
    canvas.draw_text(message, [80, 110], 40, "Red")
    canvas.draw_text(str(score)+"/"+str(attempts),[250, 20], 18, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game",300,200)

# register event handlers
start = frame.add_button("Start", start_btn_handler)
stop = frame.add_button("Stop", stop_btn_handler)
reset = frame.add_button("Reset", reset_btn_handler)
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)

# start timer and frame
frame.start()


# remember to review the grading rubric