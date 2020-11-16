# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simplegui

# helper function to start and restart the game
def new_game():
    global n
    n = 1
    return n
    
    # initialize global variables used in your code here

    # remove this when you add your code    


# define event handlers for control panel
def range100():
    global secret_number, a
    secret_number = random.randrange(0, 100)
    new_game()
    a = 7 
    print "New game. Range is [0, 100)"
    print "Number of remaining guesses is", a
    print " "
    return secret_number
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    


def range1000():
    global secret_number, a 
    secret_number = random.randrange(0, 1000)
    new_game()
    a = 10 
    print "New game. Range is [0, 1000)"
    print "Number of remaining guesses is", a
    print " "
    return secret_number
    # button that changes the range to [0,1000) and starts a new game     
    

    
def input_guess(guess):
    # main game logic goes here
    guess = int(guess)
    global n
    if guess == secret_number:
        print "Guess was", guess
        print "Number of remaining guesses is", a - n
        print "Correct!"
        print " " 
        new_game()
        if a == 7:
            range100()
        else:
            range1000()
    elif a - n == 0:
        print "Guess was", guess
        print "Number of remaining guesses is", a - n
        print "You ran out of guesses. The number was", secret_number
        print " "
        new_game()
        if a == 7:
            range100()
        else:
            range1000()
    elif guess < secret_number:
        print "Guess was", guess
        print "Number of remaining guesses is", a - n
        print "Higher!"
        print " "
        n = n + 1
        return n
    else:
        print "Guess was", guess
        print "Number of remaining guesses is", a - n
        print "Lower!"
        print " "
        n = n + 1
        return n
    
    # remove this when you add your code

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)



# register event handlers for control elements and start frame
button1 = frame.add_button("Range is [0, 100)", range100)
button2 = frame.add_button("Range is [0, 1000)", range1000)
inp = frame.add_input("Guess number", input_guess, 50)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
