#A simple Rock, Paper, Scissors program that runs 10 times and keeps score
#By: Gabriel Vidal
import random

def welcome():
    print "Welcome to Rock, Paper, Scissors!"
    print "Please enter 'rock', 'paper', or 'scissors' below. Or, press CTRL-C to quit"

def rps():


    ties = 0
    losses = 0
    wins = 0

    for i in range(10):
        computer = random.randint(1,3)
        choice = raw_input()
        choice = choice.upper()
        while not choice == "ROCK" and choice == "PAPER" and choice == "SCISSORS":
            print "Invalid input"
            choice = raw_input()
            choice = choice.upper()

        if choice == 'ROCK':
            if computer == 1:
                print "TIE"
                ties+=1
            elif computer == 2:
                print "LOSS"
                losses+=1
            elif computer == 3:
                print "WIN"
                wins+=1

            print "W:%i L:%i T:%i" % (wins, losses, ties)

        if choice == 'PAPER':
            if computer == 2:
                print "TIE"
                ties+=1
            elif computer == 3:
                print "LOSS"
                losses+=1
            elif computer == 1:
                print "WIN"
                wins+=1

            print "W:%i L:%i T:%i" % (wins, losses, ties)

        if choice == 'SCISSORS':
            if computer == 3:
                print "TIE"
                ties+=1
            elif computer == 1:
                print "LOSS"
                losses+=1
            elif computer == 2:
                print "WIN"
                wins+=1

            print "W:%i L:%i T:%i" % (wins, losses, ties)


welcome()
rps()
