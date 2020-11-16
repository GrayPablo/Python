# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simplegui

# helper function to start and restart the game
def new_game():
    global a, n
    n = 0
    a = 7 - n
    print "New game. Range is ..."
    print "Number of remaining guesses is 7"
    print " "
    return n
    
    # initialize global variables used in your code here

    # remove this when you add your code    


# define event handlers for control panel
def range100():
    global secret_number
    secret_number = random.randrange(0, 100)
    print secret_number
    return secret_number
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    


def range1000():
    global secret_number
    secret_number = random.randrange(0, 1000)
    print secret_number
    return secret_number
    # button that changes the range to [0,1000) and starts a new game     
    

    
def input_guess(guess):
    # main game logic goes here
    guess = int(guess)
    global n, a
    if a == 0:
        print "Guess was", guess
        print "Number of remaining guesses is", a
        print "You ran out of guesses. The number was", secret_number
        print " "
        new_game()
    elif guess == secret_number:
        n = n + 1
        a = 7 - n
        print "Guess was", guess
        print "Number of remaining guesses is", a
        print "Correct!"
        print " " 
        new_game()
    elif guess < secret_number:
        n = n + 1
        a = 7 - n
        print "Guess was", guess
        print "Number of remaining guesses is", a
        print "Higher!"
        print " "
        return n, a
    else:
        n = n + 1
        a = 7 - n
        print "Guess was", guess
        print "Number of remaining guesses is", a
        print "Lower!"
        print " "
        return n, a
    
    # remove this when you add your code
    pass

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)



# register event handlers for control elements and start frame
button1 = frame.add_button("Range is [0, 100)", range100)
button2 = frame.add_button("Range is [0, 1000)", range1000)
button3 = frame.add_button("New game", new_game)
inp = frame.add_input("Guess number", input_guess, 50)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
