from tkinter import *

root = Tk()


def buttonClick():
    myLabel = Label(root, text="Look I clicked the button")
    myLabel.pack()


myButton = Button(root, text="Click Me", command=buttonClick, fg="blue", bg="orange")
myButton.pack()

root.mainloop()
