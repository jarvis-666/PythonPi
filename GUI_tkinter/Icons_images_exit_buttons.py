from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning GUI using tkinter")

root.iconbitmap("C:\\Users\\Vin\\Downloads\\Custom-Icon-Design-Mono-Business-2-Coffee.ico")

my_img = Image.open("C:\\Users\\Vin\\Desktop\\edBM5X.jpg")
my_img = my_img.resize((250, 250), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(my_img)
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Button", command=root.quit)
button_quit.pack()
root.mainloop()