# "Stopwatch: The Game"
# http://www.codeskulptor.org/#user12_LrvCyEe2QIdSgLr.py

import simplegui

# define global variables
btn_width = 75
width = 200
height = 150
timer_position = [58, 86]
results_position = [156, 24]
time_value = 0
success = 0
attempts = 0

# helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global decimal_digit
    decimal_digit = t % 10
    z = t // 10
    sec = z % 60
    if sec < 10:
        seconds = "0%d" % sec
    else:
        seconds = str(sec)
    minutes = str(z // 60)
    return "%s:%s.%d" % (minutes, seconds, decimal_digit)
    
# event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer
    timer.start()
    
def stop():
    global attempts, success
    if timer.is_running():
        timer.stop()
        attempts += 1
        if decimal_digit == 0:
            success += 1

def reset():
    global time_value, success, attempts
    timer.stop()
    time_value = 0
    success = 0
    attempts = 0
    
# define event handler for timer with 0.1 sec interval
def time_update():
    global time_value
    time_value += 1
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time_value), timer_position, 36, "White")
    results = "%d / %d" % (success, attempts)
    canvas.draw_text(results, results_position, 16, "Yellow")
    
# create frame
f = simplegui.create_frame("Stopwatch", width, height)

# register event handlers
f.add_button("Start", start, btn_width)
f.add_button("Stop", stop, btn_width)
f.add_button("Reset", reset, btn_width)
f.set_draw_handler(draw)
timer = simplegui.create_timer(100, time_update)

# start frame
f.start()
