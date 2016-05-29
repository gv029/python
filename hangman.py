#hangman
#By: gv029
def hangman():
    #getting the user input for the word to be guessed
    print "Player 1: Please enter a word to be guessed"
    x = raw_input()
    x = x.upper()

    #converting the string into a list
    word = list(x)

    revealList = ["_"] * len(word)
    print " ".join(revealList)
    correct_guesses = 0
    t_guesses = 0
    wrong_guesses = t_guesses - correct_guesses

    print "Player 2: Guess a letter, followed by the RETURN key. You are allowed 6 mistakes. "


    while wrong_guesses < 6:
        if correct_guesses < len(word):
            guess = raw_input()
            guess = guess.upper()
            #looping through the list to see if the guess matches an element in word
            for i in range(len(word)):
                if guess == word[i]:
                    revealList[i] = guess
                    correct_guesses += 1

            print " ".join(revealList)
            t_guesses += 1
            wrong_guesses = t_guesses - correct_guesses


            if wrong_guesses == 6:
                print "Hangman! You lose...."
                print "The word was: %s" % "".join(word)
                exit()

            print "%i guess(es) left" % (6 - wrong_guesses)

        else:
            print "Congratulations, you win!!!"
            exit()

    #converting the list back into a string for printing
    word = "".join(word)
    revealList = "".join(revealList)
    print revealList

hangman()
