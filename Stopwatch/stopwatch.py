# Stopwatch: The Game
# Rohan Roy - 30th Oct 2013
# http://www.codeskulptor.org/#user22_aJ2B7XnzHeFpJeg.py

import simplegui

# define global variables

interval = 100
tens_sec = 0
message = "0:00.0"
score = 0
Is_timer = False
attempt = 0

# define helper function format that converts integer in A:BC.D format

def format(t):
    global message
    minutes = (t-(t%600))/600
    t = t - minutes * 600
    secs = (t-t%10)/10
    tenth = t - secs * 10
    message  = '%d:%02d.%d' % (minutes,secs,tenth)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

# Button Start
def start_btn_handler():
    global Is_timer
    timer.start()
    Is_timer = True

# Button Stop
def stop_btn_handler():
    global message
    global score
    global attempt
    global Is_timer
    timer.stop()
    if Is_timer : 
        attempt = attempt + 1
        if int(message[5]) == 0:
            score = score + 1
    Is_timer = False

# Button Reset
def reset_btn_handler():
    timer.stop()
    global tens_sec
    global score
    global attempt
    score = 0
    attempt = 0
    tens_sec = 0
    format(tens_sec)

# define event handler for timer with 0.1 sec interval

def tick():
    global tens_sec
    tens_sec = tens_sec+1
    format(tens_sec)

# define handler to draw on canvas

def draw(canvas):
    canvas.draw_text(message, [80, 110], 40, "Red")
    canvas.draw_text(str(score)+"/"+str(attempt),[250, 20], 18, "Green")
    
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
