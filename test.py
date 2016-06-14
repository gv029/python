from Tkinter import *

root = Tk() #initializes main window

def printName(event):
    print "my name is Hal"

button1 = Button(root, text="printName")

button1.bind("<Button-1>",printName)
button1.pack()

#Exit on close
root.mainloop()
