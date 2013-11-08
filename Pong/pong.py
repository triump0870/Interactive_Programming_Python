# Implementation of classic arcade game Pong
# Rohan Roy - 6th Nov 2013
# http://www.codeskulptor.org/#user23_alOd8kS55ui1Z17.py

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
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, RIGHT, LEFT # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [random.randrange(2,4), -random.randrange(1,3)]
    if direction != RIGHT:
        ball_vel[0] = -ball_vel[0]
    else:
        pass

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, hit1, hit2, ls, l # these are ints
    score1 = 0
    score2 = 0
    hit1 = 0
    hit2 = 0
    ls = 0
    l = []
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    spawn_ball(True)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, hit1, hit2, ls
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] - BALL_RADIUS < PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] =  ball_vel[1] * 1.1
            hit1 += 1
            ls += 1
        else:
            score2 += 1
            spawn_ball(True)
            l.append(ls)
            ls = 0
    elif ball_pos[0] + BALL_RADIUS > WIDTH - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] =  ball_vel[1] * 1.1
            hit2 += 1
            ls += 1
        else:
            score1 += 1
            spawn_ball(False)
            l.append(ls)
            ls = 0
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "white", "white")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] + paddle1_vel[1] >= HALF_PAD_HEIGHT and paddle1_pos[1] + paddle1_vel[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel[1]
    if paddle2_pos[1] + paddle2_vel[1] >= HALF_PAD_HEIGHT and paddle2_pos[1] + paddle2_vel[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel[1]
        
    # draw paddles
    c.draw_line((paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT), (paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT), PAD_WIDTH, "green")
    c.draw_line((paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT), (paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT), PAD_WIDTH, "red")
    
    # longest streak
    t = 0
    if len(l) > 0:
        t = max(l)
    
    # draw scores
    c.draw_text("Player1", [180, 30], 20, "green")
    c.draw_text("Player2", [340, 30], 20, "red")
    c.draw_text(str(score1), [210, 60], 30, "green")
    c.draw_text(str(score2), [370, 60], 30, "red")
    c.draw_text("Total Hits", [18, 30], 20, "green") 
    c.draw_text(str(hit1), [60, 60], 30, "green")
    c.draw_text("Total Hits", [472, 30], 20, "red")
    c.draw_text(str(hit2), [515, 60], 30, "red")   
    c.draw_text("Current Streak:", [130,360], 20, "green")
    c.draw_text(str(ls), [310, 362], 30, "red")
    c.draw_text(str(t), [310,392] ,30, "red")
    c.draw_text("Longest Streak:", [130,390] ,20, "green")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if chr(key) == "w" or chr(key) == "W":
        paddle1_vel[1] = -3
    elif chr(key) == "s" or chr(key) == "S":
        paddle1_vel[1] =  3
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -3
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] =  3
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if chr(key) == "w" or chr(key) == "W":
        paddle1_vel[1] =  0
    elif chr(key) == "s" or chr(key) == "S":
        paddle1_vel[1] =  0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] =  0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] =  0       

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)
frame.set_canvas_background("#001f1f")

# start frame
new_game()
frame.start()
