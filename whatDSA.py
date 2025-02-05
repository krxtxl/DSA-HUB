import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)

def open_choose():
    root.destroy()
    subprocess.Popen(["python", "choose_tab.py"])

def back_start():
    root.destroy()
    subprocess.Popen(["python", "cover.py"])
root = tk.Tk()
root.geometry("1280x720")
root.configure(bg="#770F1A")
root.title("What is Data Structure and Algorithms?")

frame = tk.Frame(root, bg='#770F1A')
frame.pack(fill='both', expand=True)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

image_path = "dsatitle.png"
image = resize_image(image_path, 600, 130)
image_label = tk.Label(frame, image=image, bg="#770F1A")
image_label.grid(column=0, columnspan=2, row=0, padx=(0,0), pady=(0, 0), sticky="n")

description_text = (
    "A data structure is a method of organizing data in a computer for efficient use and optimal algorithm performance."
    "It is based on the choice of an abstract data type (ADT). \n"
    "   \n"
    "A well-designed data structure allows for critical operations using minimal resources, execution time, and memory space."
    "A data structure addresses two fundamental concerns: data storage and operations.\n"
    "   \n"
    "The functional definition of a data structure, known as ADT, is independent of implementation."
    "Common data structures include lists, arrays, stacks, queues, heaps, trees, and graphs. "
)

description_label = tk.Label(frame, text=description_text, font=("Arial Narrow", 20), fg="white", bg="#770F1A", justify="left", wraplength=600)
description_label.grid(column=0, row=0, padx=(60,0), pady=(180,0), sticky="w")

dsa_path = "dsa.png"
dsa = resize_image(dsa_path, 550, 500)
dsa_label = tk.Label(frame, image=dsa, bg="#770F1A")
dsa_label.grid(column=1, row=0, padx=0, pady=(140,0), sticky="w")

button_picture_path_practice = "learn_more.png"
button_picture_practice = resize_image(button_picture_path_practice, 168, 40)
practice_button = tk.Button(frame, image=button_picture_practice, highlightthickness=0, relief='flat', borderwidth=0, command=open_choose)
practice_button.grid(column=1, row=0, padx=(300,0), pady=(560,0), sticky="w")

button_picture_path_back = "back.png"
button_picture_back = resize_image(button_picture_path_back, 168, 40)
back_button = tk.Button(frame, image=button_picture_back, highlightthickness=0, relief='flat', borderwidth=0, command=back_start)
back_button.grid(column=1, row=0, padx=(300, 0), pady=(660, 0), sticky="w")

root.mainloop()
