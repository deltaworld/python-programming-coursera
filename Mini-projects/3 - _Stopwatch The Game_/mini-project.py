# http://www.codeskulptor.org/#user12_lRHfq13PE0sVr8q_1.py
# template for "Stopwatch: The Game"
import simplegui
import math
# define global variables
counter = 0
stop_counter = 0
stop_seconds = 0
display = "0:00.0"


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    t = t/10
    fractions = t % 10
    #fractions = int(fractions * 10) % 10
    fractions = int((((t % 10) * 10) % 10) * 100) / 100
    fractions = math.ceil(fractions)
    
    #print fractions
    int_t = int(t)
    minutes = int_t // 60
    seconds = int_t % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    return str(minutes) + ":" + str(seconds) + "." + str(fractions)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global stop_counter, stop_seconds
    stop_counter += 1
    if counter % 10 == 0:
        stop_seconds += 1
    timer.stop()

def reset():
    global counter, display, stop_counter, stop_seconds
    timer.stop()
    stop_counter = 0
    stop_seconds = 0
    counter = 0
    display = format(counter)
    pass

# define event handler for timer with 0.1 sec interval
def tick():
    
    global counter, display
    counter = counter + 1
    #print counter
    #print format(counter)
    display = format(counter)

# define draw handler
def draw(canvas):
    game_counter = str(stop_seconds) + "/" + str(stop_counter)
    canvas.draw_text(display, [90,160], 48, "White")
    canvas.draw_text(game_counter, [250,30], 25, "White")
        
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

# start frame
frame.start()
#timer.start()
# Please remember to review the grading rubric

format(00)