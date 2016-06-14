#hangman GUI version
#By: gv029
from Tkinter import *
import random

root = Tk()

word = ['P','Y','T','H','O','N']
solution = ["_"]*len(word)

entry1 = Entry()
entry1.pack()

greeting = Label(root, text="Welcome to hangman!")
greeting.pack()

def getguess():

    guess = entry1.get()
    guess = guess.upper()


    label1 = Label(root, text=guess)
    label1.pack()
    root.update()

    #entry1.delete(0,'end')
    return guess


def compare(word, guess, solution):
    for i in range(len(word)):
        if guess == word[i]:
            solution[i] = guess

        print solution
        return solution

def g_and_c(event):
    getguess()
    compare(word,getguess(),solution)









button1 = Button(root, text="guess")
button1.bind("<Button-1>",g_and_c)
button1.pack()


root.mainloop()
