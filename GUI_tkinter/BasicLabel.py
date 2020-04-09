from tkinter import *
# button, frame, text widgets
# create a root widget, which is a box window

root = Tk()     # first thing for tkinter

# define create a widget and display it

# Creating a label widget
myLabel = Label(root, text="Hello from Vinayak")
myLabel.pack()      # shoving it onto the screen

root.mainloop()     # this loop runs until closed
