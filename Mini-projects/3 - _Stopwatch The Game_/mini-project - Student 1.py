# template for "Stopwatch: The Game"
#http://www.codeskulptor.org/#user12_TQpHp84oku_0.py

import simplegui
# define global variables
t=0
stopwatch = True
att = 0
cor = 0
string1 = "0:00.0"
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global string1
    mili = t%10
    seconds = ((t-mili)/10)%60
    minutes = t//600
    if(seconds<10):
        string1 = str(minutes)+":0"+str(seconds)+"."+str(mili)
       
    else:
        string1 = str(minutes)+":"+str(seconds)+"."+str(mili)
    return string1
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopwatch
    timer.start()
    stopwatch = True

def stop():
    global stopwatch,att,cor
    timer.stop()
    
    if(stopwatch == True):
        att = att + 1
        if(t%10 == 0):
              cor = cor + 1
    stopwatch = False
def reset():
    global stopwatch ,att, cor, t
    timer.stop()
    t=0
    stopwatch = False
    att = 0
    cor = 0

    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t = t+1 

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), (150, 200), 48, "White")
    canvas.draw_text(str(cor)+"/"+str(att), (250, 50), 24, "Red")
# create frame
frame = simplegui.create_frame("Stopwatch",400,400)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
# register event handlers
timer = simplegui.create_timer(100, timer_handler)
button1 = frame.add_button("Start", start)
button2 = frame.add_button("Stop", stop)
button3 = frame.add_button("Reset", reset)
# start frame
frame.start()
# Please remember to review the grading rubric
