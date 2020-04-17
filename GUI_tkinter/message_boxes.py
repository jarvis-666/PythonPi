from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message boxes")

def popup():
    response = messagebox.askquestion(title="This is the title", message="Hello Vinayak!")
    if response == "yes":
        Label(root, text="Yes Clicked").pack()
    else:
        Label(root, text="No Clicked").pack()

my_button = Button(root, text="PopUp", command=popup).pack()
# print(*dir(messagebox))

root.mainloop()