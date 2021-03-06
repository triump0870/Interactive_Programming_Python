# implementation of card game - Memory
# Rohan Roy - 15th Nov, 2013

import simplegui
import random
import math

# Global Variables
WIDTH = 800
HEIGHT = 100
moves = 0

# helper function to initialize globals
def init():
    global numbers
    global exposed
    global linepos
    global state
    global cards
    global moves
    moves = 0
    state = 0
    cards = ['0','0']
    numbers = [ i+1 if i < 8 else i-7 for i in range(16)]
    random.shuffle(numbers)
    exposed = [ False for i in range(16)]
    linepos = [25 + WIDTH/16*i for i in range(16)]	

# define event handlers
def mouseclick(pos):
    global exposed
    global linepos
    global state
    global cards
    global moves
    
    for i in range(16):
        if math.fabs(pos[0] - linepos[i]) < 22.5:
            if state == 0:
                state = 1
                cards[0] = i
                exposed[i] = True
            elif state == 1:
                if exposed[i] == False:
                    exposed[i] = True
                    state = 2
                    cards[1] = i
                    moves += 1
            elif state == 2:
                if exposed[i] == False:
                    exposed[i] = True
                    state = 1
                    if numbers[cards[0]] != numbers[cards[1]]:
                        exposed[cards[0]] = False
                        exposed[cards[1]] = False
                    cards[0] = i
                               
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global numbers
    global exposed
    space = 5
    l.set_text("Moves = " + str(moves))
    for i in range(len(numbers)):
        if exposed[i]: 
            canvas.draw_text(str(numbers[i]), (linepos[i]-20, 80), 60, "Blue")
        else:
            canvas.draw_line((linepos[i], 0), (linepos[i], HEIGHT), 45, "green")
        space = space + WIDTH/16
     
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

# Always remember to review the grading rubric
