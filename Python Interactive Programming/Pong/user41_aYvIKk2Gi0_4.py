# Implementation of classic arcade game Pong

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
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1, score2 = 0, 0
    paddle1_pos, paddle2_pos = [0, HEIGHT/2], [WIDTH, HEIGHT/2]
    paddle1_vel, paddle2_vel = 0, 0
    direction = random.choice([LEFT, RIGHT])
    spawn_ball(direction)
 
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction == LEFT:
        ball_pos =[WIDTH/2, HEIGHT/2]
        ball_vel[0] = - random.randrange(120, 240)/60
        ball_vel[1] = - random.randrange(60, 180)/60
    else:
        ball_pos = [WIDTH/2, HEIGHT/2]
        ball_vel[0] = random.randrange(120, 240)/60
        ball_vel[1] = - random.randrange(60, 180)/60
   
def update_ball():
    global ball_pos, ball_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif HEIGHT - ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
  
def update_paddle():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    if paddle1_pos[1] <= 40:
        paddle1_pos[1] += 1
    elif HEIGHT - paddle1_pos[1] <= 40:
        paddle1_pos[1] -= 1
    elif paddle2_pos[1] <= 40:
        paddle2_pos[1] += 1
    elif HEIGHT - paddle2_pos[1] <= 40:
        paddle2_pos[1] -= 1
    else:
        paddle1_pos[1] += paddle1_vel
        paddle2_pos[1] += paddle2_vel
    
def ball_collide():
    global ball_pos, ball_vel, score1, score2
    if ball_pos[0] <= BALL_RADIUS:
        if abs(ball_pos[1] - paddle1_pos[1]) <= 40:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] = ball_vel[0] * 1.1
        else:
            spawn_ball(RIGHT)
            score2 += 1
    elif WIDTH - ball_pos[0] <= BALL_RADIUS:
        if abs(ball_pos[1] - paddle2_pos[1]) <= 40:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] = ball_vel[0] * 1.1
        else:    
            spawn_ball(LEFT)
            score1 += 1

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # update ball
    update_ball()
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 5, 'White', 'White')
    # update paddle's vertical position, keep paddle on the screen
    update_paddle()
    # draw paddles 
    canvas.draw_line([4, paddle1_pos[1] - HALF_PAD_HEIGHT], [4, paddle1_pos[1] + HALF_PAD_HEIGHT], 8, 'Blue')
    canvas.draw_line([596, paddle2_pos[1] - HALF_PAD_HEIGHT], [596, paddle2_pos[1] + HALF_PAD_HEIGHT], 8, 'Red')
    # determine whether paddle and ball collide    
    ball_collide()
    # draw scores
    canvas.draw_text(str(score1), [250, 50], 35, 'White')
    canvas.draw_text(str(score2), [350, 50], 35, 'White')
    
def keydown(key):
    vel = 10
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= vel
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += vel
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= vel
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('Restart game', new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
