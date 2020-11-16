# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
tries = 7
attemps = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, maximum, minimum, attemps
    attemps = 0
    if tries == 7:
        secret_number = random.randrange(0, 100)
        maximum = 99
        print 'New game. Range is [0, 100).'
        print 'Number of remaining guesses is ' + str(tries) + '.'
        print ' '
    else:
        secret_number = random.randrange(0, 1000)
        maximum = 999
        print 'New game. Range is [0, 1000).'
        print 'Number of remaining guesses is ' + str(tries) + '.'
        print ' '
    # remove this when you add your code    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, tries, attemps
    secret_number = random.randrange(0, 100)
    tries = 7
    attemps = 0
    new_game()
    # remove this when you add your code    


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, tries, attemps
    secret_number = random.randrange(0, 1000)
    tries = 10
    attemps = 0
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global tries, attemps
    guess = int(guess)
    attemps += 1
    if (attemps - tries) == 0:
        if guess == secret_number:
            print 'Guess was ' + str(guess) + '.'
            print 'Number of remaining guesses is ' + str(tries - attemps) + '.'
            print 'You win!'
            print ' '
        else:
            print 'Guess was ' + str(guess) + '.'
            print 'You ran out of guesses.'
            print 'Secret number was ' + str(secret_number) + '.'
            print ' '
        attemps = 0
        new_game()

    else:
        if guess > maximum or guess < 0:
            attemps -= 1
            print 'Number out of range!'
            print 'Range is ' + '[0, ' + str(maximum + 1) + ').'
            print 'Number of remaining guesses is ' + str(tries - attemps) + '.'
            print ' '
        elif guess == secret_number:
            print 'Guess was ' + str(guess) + '.'
            print 'Number of remaining guesses is ' + str(tries - attemps) + '.'
            print 'You win!'
            print ' '
            new_game()
        elif guess < secret_number:
            print 'Guess was ' + str(guess) + '.'
            print 'Number of remaining guesses is ' + str(tries - attemps) + '.'
            print 'Higher!'
            print ' '
        else:
            print 'Guess was ' + str(guess) + '.'
            print 'Number of remaining guesses is ' + str(tries - attemps) 
            print 'Lower!'
            print ' '

    # remove this when you add your code

    
# create frame
frame = simplegui.create_frame("Guess the number!", 175, 175)
frame.add_input("Choose number", input_guess, 100)
frame.add_button("Range [0, 100)", range100, 120)
frame.add_button("Range [0, 1000)", range1000, 120)
# register event handlers for control elements and start frame


# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
