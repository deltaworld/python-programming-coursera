# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user12_dhir7wbA3c3EDqr_1.py

import simplegui



# define global variables
width = 300
height = 300
our_time  = 0
attempts = 0
success = 0




# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    m = t//(60*1000)
    s =  (t - m*(60*1000)) // 1000
    th = (t - m*(60*1000) - s*1000) // 100
    s = str(s)
    if len(s) == 1:
        s = "0"+s
    return str(m)+":"+str(s)+"."+str(th)
   
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer
    timer.start()

def stop():
    global timer
    if  timer.is_running():
        timer.stop()
        global  attempts, success
        attempts += 1
        if format(our_time).find(".0") > 0:
            success += 1
        


def reset():
    global timer
    if  timer.is_running():    
        stop()
    global our_time,  attempts, success
    attempts = 0
    success = 0
    our_time = 0

    
# define event handler for timer with 0.1 sec interval
def timer_handler():
  global our_time
  our_time += 100
    
 
    
timer = simplegui.create_timer(100, timer_handler)

# define draw handler
def draw(canvas):
    global width, height 
    text = format(our_time)
    canvas.draw_text(text, (width//2-(len(text)//2)*25, height//2), 50, "Yellow", "sans-serif")
    canvas.draw_text(str(success)+'/'+str(attempts), (240,30), 30, "Teal", "sans-serif")
    
    
# create frame
fr =  simplegui.create_frame('"Stopwatch: The Game"  Project', width, height, width)

# register event handlers
button1 = fr.add_button("Start", start, width)
button2 = fr.add_button("Stop", stop, width)
button3 = fr.add_button("Reset", reset, width)
fr.set_draw_handler(draw)

# start frame
fr.start()

# Please remember to review the grading rubric



