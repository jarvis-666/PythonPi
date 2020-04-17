from tkinter import *

root = Tk()
root.title("Working with radio buttons")

# r = IntVar()    # allows tkinter to keep changes that happen
# r.set(2)

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Chicken", "Chicken")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked_radio(option):
    my_label = Label(root, text=f"Option {option} selected")
    my_label.pack()

# Radiobutton(root, text="Option1", variable=r, value=1, command=lambda: clicked_radio(r.get())).pack()
# Radiobutton(root, text="Option2", variable=r, value=2, command=lambda: clicked_radio(r.get())).pack()

# my_label = Label(root, text=f"Option {pizza.get()} selected")
my_button = Button(root, text="Click for selection", command=lambda: clicked_radio(pizza.get()))

# my_label.pack()
my_button.pack()
root.mainloop()