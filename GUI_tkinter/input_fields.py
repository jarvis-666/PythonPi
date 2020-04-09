from tkinter import *

root = Tk()
# creating an entry widget which is an input area for the user
e = Entry(root, width=50)
e.insert(0, "Enter your name: ")
e.pack()

def button_click():
    label_name = Label(root, text="Hello " + e.get())
    label_name.pack()

button = Button(root, text="Enter", command=button_click)
button.pack()
root.mainloop()