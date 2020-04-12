from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer App")
root.iconbitmap("C:\\Users\\Vin\\Downloads\\Custom-Icon-Design-Mono-Business-2-Coffee.ico")

image_path_list = ["C:\\Users\\Vin\\Pictures\\Barkha Singh (@barkhasingh0308) • Instagram photos and videos_files\\28151942_1590228827730166_2718671391644712960_n.jpg", "C:\\Users\\Vin\\Pictures\\Barkha Singh (@barkhasingh0308) • Instagram photos and videos_files\\28151531_1600130836729124_5229439728775856128_n.jpg",\
                   "C:\\Users\\Vin\\Pictures\\Barkha Singh (@barkhasingh0308) • Instagram photos and videos_files\\28157929_1592720374147155_5795898356945387520_n.jpg", "C:\\Users\\Vin\\Pictures\\Barkha Singh (@barkhasingh0308) • Instagram photos and videos_files\\29095587_2137318386284299_5517000210288476160_n.jpg"]

my_img0 = Image.open(image_path_list[0])
my_img0 = my_img0.resize((500, 500), Image.ANTIALIAS)
my_img0 = ImageTk.PhotoImage(my_img0)

my_img1 = Image.open(image_path_list[1])
my_img1 = my_img1.resize((500, 500), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(my_img1)

my_img2 = Image.open(image_path_list[2])
my_img2 = my_img2.resize((500, 500), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(my_img2)

my_img3 = Image.open(image_path_list[3])
my_img3 = my_img3.resize((500, 500), Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(my_img3)

my_img_list = [my_img0, my_img1, my_img2, my_img3]

status = Label(root, text=f"Image 1 of {len(my_img_list)}", bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img_list[0])
my_label.grid(row=0, column=0, columnspan=3)


def next_button(image_number):
    global my_label
    global button_next
    global button_previous

    my_label.grid_forget()      # to delete the current image
    my_label = Label(image=my_img_list[image_number - 1])
    button_next = Button(root, text=">>>", command=lambda: next_button(image_number + 1))
    button_previous = Button(root, text="<<<", command=lambda: previous_button(image_number - 1))

    if image_number == 4:   # Disable the button when all images seen
        button_next = Button(root, text=">>>", command=lambda: next_button(1))

    # Updated Status Bar
    status = Label(root, text=f"Image {image_number} of {len(my_img_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_previous.grid(row=1, column=0)

def previous_button(image_number):
    global my_label
    global button_next
    global button_previous

    my_label.grid_forget()  # to delete the current image
    my_label = Label(image=my_img_list[image_number - 1])
    button_next = Button(root, text=">>>", command=lambda: next_button(image_number + 1))
    button_previous = Button(root, text="<<<", command=lambda: previous_button(image_number - 1))

    if image_number == 1:  # Disable the button when all images seen
        button_previous = Button(root, text="<<<", command=lambda: previous_button(4))

    # Updated Status bar
    status = Label(root, text=f"Image {image_number} of {len(my_img_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_previous.grid(row=1, column=0)


button_previous = Button(root, text="<<<", state=DISABLED)
button_next = Button(root, text=">>>", command=lambda: next_button(2))
button_quit = Button(root, text="Exit Button", command=root.quit)

button_next.grid(row=1, column=2)
button_previous.grid(row=1, column=0)
button_quit.grid(row=1, column=1, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()