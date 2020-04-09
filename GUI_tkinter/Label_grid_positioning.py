from tkinter import *

root = Tk()     # creating the initial window

# Creating labels
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Vinayak")

myLabel1.grid(row=0, column=0)      # instead of pack() now we are using grid(), which creates a coordinate system
myLabel2.grid(row=1, column=5)
# Note that position is relative
# tkinter ignores the blank area
# HACK: we can always insert blank labels to position things properly

root.mainloop()