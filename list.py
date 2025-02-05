import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)

def open_list():
    root.destroy()
    script_path = "list_practice.py"
    subprocess.Popen(["python", "list_practice.py"])

def back_choose():
    root.destroy()
    subprocess.Popen(["python", "choose_tab.py"])

root = tk.Tk()
root.geometry("1280x720")
root.configure(bg="#770F1A")
root.title("Stack")

frame = tk.Frame(root, bg='#770F1A')
frame.pack(fill='both', expand=True)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

title_image_path = "list_button.png"
title_image = resize_image(title_image_path, 600, 155)
title_image_label = tk.Label(frame, image=title_image, bg="#770F1A")
title_image_label.grid(column=0, row=0, padx=(0, 0), pady=(25, 0), sticky="nw")

description_text = (
    "   \n"
    "The list can be defined as an abstract data type in which the elements are stored in an ordered manner for easier and efficient retrieval of the elements.\n"
    "   \n"
    "List Data Structure allows repetition that means a single piece of data can occur more than once in a list. In the case of multiple entries of the same data, each entry of that repeating data is considered as a distinct item or entry. \n"
    "   \n"
    "It is very much similar to the array but the major difference between the array and the list data structure is that array stores only homogenous data in them whereas the list (in some programming languages) can store heterogeneous data items in its object. List Data Structure is also known as a sequence."
)

description_label = tk.Label(
    frame, text=description_text, font=("Arial Narrow", 20), fg="white", bg="#770F1A", justify="left", wraplength=600
)

description_label.grid(column=0, row=0, padx=(60,0), pady=(150,0), sticky="w")

image_path = "list_picture.png"
image = resize_image(image_path, 440, 380)
image_label = tk.Label(frame, image=image, bg="#770F1A")
image_label.grid(column=1, row=0, padx=(50,0), pady=(90,0), sticky="w")

button_picture_path_practice = "practice.png"
button_picture_practice = resize_image(button_picture_path_practice, 168, 40)
practice_button = tk.Button(frame, image=button_picture_practice, highlightthickness=0, relief='flat', borderwidth=0, command=open_list)
practice_button.grid(column=1, row=0, padx=(300,0), pady=(550,0), sticky="w")

button_picture_path_back = "back.png"
button_picture_back = resize_image(button_picture_path_back, 168, 40)
back_button = tk.Button(frame, image=button_picture_back, highlightthickness=0, relief='flat', borderwidth=0, command=back_choose)
back_button.grid(column=1, row=0, padx=(300, 0), pady=(650, 0), sticky="w")

root.mainloop()