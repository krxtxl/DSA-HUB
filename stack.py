import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)

def open_practice_window():
    root.destroy()
    subprocess.Popen(["python", "stack_practice.py"])

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

title_image_path = "stackname.png"
title_image = resize_image(title_image_path, 600, 155)
title_image_label = tk.Label(frame, image=title_image, bg="#770F1A")
title_image_label.grid(column=0, row=0, padx=(0, 0), pady=(50, 0), sticky="nw")

description_text = (
    "A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means the last element added to the stack\n"
    " is the first one to be removed.\n"
    "It behaves like a stack of plates, where the last plate added is the first one to be removed.\n\n"
    "Key operations:\n"
    "    ▻ Push: Add an element to the top of the stack.\n"
    "    ▻ Pop: Remove the top element from the stack.\n"
    "    ▻ Peek: View the top element without removing it."
)

description_label = tk.Label(
    frame, text=description_text, font=("Arial Narrow", 18), fg="white", bg="#770F1A", justify="left", wraplength=600
)
description_label.grid(column=0, row=0, padx=(60,0), pady=(160,0), sticky="w")

image_path = "stack.png"
image = resize_image(image_path, 500, 300)
image_label = tk.Label(frame, image=image, bg="#770F1A")
image_label.grid(column=1, row=0, padx=0, pady=(160,0), sticky="w")

button_picture_path_practice = "practice.png"
button_picture_practice = resize_image(button_picture_path_practice, 168, 40)
practice_button = tk.Button(frame, image=button_picture_practice, highlightthickness=0, relief='flat', borderwidth=0, command=open_practice_window)
practice_button.grid(column=1, row=0, padx=(300,0), pady=(550,0), sticky="w")

button_picture_path_back = "back.png"
button_picture_back = resize_image(button_picture_path_back, 168, 40)
back_button = tk.Button(frame, image=button_picture_back, highlightthickness=0, relief='flat', borderwidth=0, command=back_choose)
back_button.grid(column=1, row=0, padx=(300, 0), pady=(650, 0), sticky="w")

root.mainloop()