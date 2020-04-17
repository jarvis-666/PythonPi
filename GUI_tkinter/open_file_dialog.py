from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Opening Files")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:\\Users\\Vin\\sarahkhatri", title="Select a file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    my_image = ImageTk.PhotoImage(Image.open(root.filename).resize((400, 500), Image.ANTIALIAS))
    Label(root, image=my_image).pack()

my_button = Button(root, text="Open a file", command=open)
my_button.pack()

root.mainloop()
