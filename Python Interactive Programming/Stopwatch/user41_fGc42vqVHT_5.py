# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
n = 0
a = 0
A = 0
B = 0
C = 0
D = 0
stopwatch = "0" + ":" + "00" + "." + "0"
success = 0
tries = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global stopwatch, A, B, C, D 
    D = t % 10
    if t % 10 == 0:
        C += 1
        C = C % 10
    if t % 100 == 0:
        B += 1
        B = B % 6
    if t % 600 == 0:
        A += 1
    stopwatch = str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def stopwatch_start():
    timer.start()
def stopwatch_stop():
    timer.stop()
    global a, success, tries
    if D == 0 and a == n:
        success += 0
        tries += 0
    elif D == 0:
        success += 1
        tries += 1
        a = n
    elif D != 0 and a == n:
        success += 0
        tries += 0
    else:
        tries += 1
        a = n
        
def stopwatch_reset():
    global n, stopwatch, A, B, C, D, success, tries
    n = 0
    a = 0
    A = 0
    B = 0
    C = 0
    D = 0
    stopwatch = "0" + ":" + "00" + "." + "0"
    success = 0
    tries = 0
    timer.stop()
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global stopwatch, n
    n += 1
    format(n)

timer = simplegui.create_timer(100, timer_handler)

# define draw handler
def draw_handler(canvas):
    score = str(success) + "/" + str(tries)
    canvas.draw_text(stopwatch, [120, 150], 30, 'Red')
    canvas.draw_text(score, [270, 20], 20, 'Yellow')
    
# create frame
frame = simplegui.create_frame ("Stopwatch: The Game", 300, 300)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", stopwatch_start)
frame.add_button("Stop", stopwatch_stop)
frame.add_button("Reset", stopwatch_reset)
# start frame
frame.start()

# Please remember to review the grading rubric
