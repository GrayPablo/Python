# template for "Stopwatch: The Game"
import simplegui
# define global variables
A = 0
B = 0
C = 0
D = 0
tenths = 0
running = False
tries = 0
success = 0
colour = "White"
WIDTH = 300
HEIGHT = 200

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A, B, C, D
    D = t % 10
    C = (t // 10) % 10
    B = (t // 100) % 6
    A = t // 600
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def time_start():
    global running, color
    colour = "White"
    frame.set_canvas_background(colour)
    running = True

def time_stop():
    global running, tries, success, colour
    if running == True:
        if D == 0:
            tries += 1
            success += 1
            colour = "Green"
        else:
            tries += 1
            colour = "Red"
    frame.set_canvas_background(colour)
    running = False
    
def time_reset():
    global A, B, C, D, tenths, tries, success, running, colour
    running = False
    colour = "White"
    frame.set_canvas_background(colour)
    A, B, C, D, tenths, tries, success = 0, 0, 0, 0, 0, 0, 0

# define event handler for timer with 0.1 sec interval
def time_handler():
    global tenths, running
    if running == True:
        tenths += 1
# define draw handler
def draw_handler(canvas):
        canvas.draw_text(format(tenths), [WIDTH / 2 - 35, HEIGHT / 2],
                         30, "Black")
        canvas.draw_text("Score: " + str(success) +
                         "/" + str(tries), 
                         [7 * WIDTH / 10 - 5, HEIGHT / 8], 20, "Black")
        
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", WIDTH, HEIGHT)

# register event handlers
start_button = frame.add_button("Start", time_start, 150)
stop_button = frame.add_button("Stop", time_stop, 150)
reset_button = frame.add_button("Reset", time_reset, 150)
timer = simplegui.create_timer(100, time_handler)
timer.start()
frame.set_draw_handler(draw_handler)
frame.set_canvas_background(colour)
# start frame
frame.start()

# Please remember to review the grading rubric
