from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Creating a new window")


def open():
    global my_image     # This is a fix to open an image in second window
    top = Toplevel()
    top.title("This is the secondary window")
    my_image = Image.open("C:\\Users\\Vin\\sarahkhatri\\2020-04-07_08-10-57_UTC.jpg")
    my_image = my_image.resize((400, 500), Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(my_image)
    label = Label(top, image=my_image).pack()
    button_close = Button(top, text="Close Window", command=top.destroy).pack()

button = Button(root, text="Click me!", command=open).pack()

root.mainloop()