# implementation of card game - Memory

import simplegui
import random
WIDTH = 800
HEIGHT = 100
state = 0
turns = 0
# helper function to initialize globals
def new_game():
    global deck, exposed, seen, state, turns, card_index
    list1 = range(8)
    list2 = range(8)
    state = 0
    turns = 0
    seen = []
    card_index = []
    deck = list1 + list2
    random.shuffle(deck)
    exposed = range(len(deck))
    for i in range(len(deck)):
        exposed[i] = False 
    label.set_text("Turns = " + str(turns))
    
""" seen stores the values of all exposed cards """
""" card_index stores the index of seen cards """ 

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, turns, card_index
    if exposed[pos[0] * 16 / WIDTH] == False:
        if state == 0:
            state = 1
            exposed[pos[0] * 16 / WIDTH] = True
            seen.append(deck[pos[0] * 16 / WIDTH])
            card_index.append(pos[0] * 16 / WIDTH)
        elif state == 1:
            state = 2
            exposed[pos[0] * 16 / WIDTH] = True
            seen.append(deck[pos[0] * 16 / WIDTH])
            card_index.append(pos[0] * 16 / WIDTH)
            turns += 1
            label.set_text("Turns = " + str(turns))
        else:
            if seen[len(seen) - 1] != seen[len(seen) - 2]:
                card_index.pop(), card_index.pop()
                card_index.append(pos[0] * 16 / WIDTH)
                for i in range(len(exposed)):
                    exposed[i] = False
                exposed[pos[0] * 16 / WIDTH] = True
                for n in card_index:
                    exposed[n] = True
            else:
                exposed[pos[0] * 16 / WIDTH] = True
                card_index.append(pos[0] * 16 / WIDTH)
            state = 1
            seen.append(deck[pos[0] * 16 / WIDTH])
                      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    for n in range(len(deck)):
        if exposed[n] == False:
            canvas.draw_polygon([(n * WIDTH / 16, 0),
                ((n + 1) * WIDTH / 16, 0),
                ((n + 1) * WIDTH / 16, HEIGHT),
                (n * WIDTH / 16, HEIGHT)],
                 5, 'Black', 'Green')
        else:
            canvas.draw_text(str(deck[n]),
                            ((n * WIDTH / 16)+ 10,
                             0.75 * HEIGHT), 3 * HEIGHT / 5, 'White')



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric