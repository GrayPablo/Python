# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else: 
        return "that is not a correct name!"

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else: 
        return "that is not a correct name!"

def rpsls(player_choice): 
    import random
    player_number = name_to_number(player_choice) 
    comp_number = random.randrange(0,5)
    
    print "Player chooses", number_to_name(player_number)
    print "Computer chooses", number_to_name(comp_number)
   
    if player_number == comp_number:
        print "Player and Computer tie!"
        return " "
    elif (player_number - comp_number) % 5 == 1:
        print "Player wins!"
        return " "
    elif (player_number - comp_number) % 5 == 2:
        print "Player wins!"
        return " "
    else:
        print "Computer wins!"
        return " "
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
print rpsls("rock")
print rpsls("Spock")
print rpsls("paper")
print rpsls("lizard")
print rpsls("scissors")

# always remember to check your completed program against the grading rubric


