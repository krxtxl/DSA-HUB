import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)

def what_DSA():
    choose_window.destroy()
    subprocess.Popen(["python", "whatDSA.py"])

choose_window = tk.Tk()
choose_window.geometry("1280x720")
choose_window.configure(bg="#770F1A")
choose_window.title("Topics")

frame = tk.Frame(choose_window, bg='#770F1A')
frame.pack(fill='both', expand=True)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)

image_path = "about.png"
image = resize_image(image_path, 600, 130)
image_label = tk.Label(frame, image=image, bg="#770F1A")
image_label.grid(column=0, columnspan=3, row=0, padx=(30,0), pady=(30, 20), sticky="nw")

canvas = tk.Canvas(frame, bg="#770F1A", highlightthickness=0, width=1200, height=10)
canvas.grid(column=0, columnspan=3, row=0, pady=(140, 0), sticky="n")
canvas.create_line(0, 5, 1200, 5, fill="white", width=3)

def open_stack():
    choose_window.destroy()
    subprocess.Popen(["python", "stack.py"])

stackb_picture_path = "stackb.png"
stackb_picture = resize_image(stackb_picture_path, 220, 90)
stackb_button = tk.Button(frame, image=stackb_picture, highlightthickness=0, relief='flat', borderwidth=0, command=open_stack)
stackb_button.grid(column=0, row=1, padx=(100, 0), sticky="n")

def open_list():
    choose_window.destroy()
    subprocess.Popen(["python", "list.py"])

listb_picture_path = "listb.png"
listb_picture = resize_image(listb_picture_path, 220, 90)
listb_button = tk.Button(frame, image=listb_picture, highlightthickness=0, relief='flat', borderwidth=0, command=open_list)
listb_button.grid(column=1, row=1, sticky="n")

def open_array():
    choose_window.destroy()
    subprocess.Popen(["python", "array.py"])

arrayb_picture_path = "arrayb.png"
arrayb_picture = resize_image(arrayb_picture_path, 220, 90)
arrayb_button = tk.Button(frame, image=arrayb_picture, highlightthickness=0, relief='flat', borderwidth=0, command=open_array)
arrayb_button.grid(column=2, row=1, padx=(0, 100), sticky="n")

def open_trees():
    choose_window.destroy()
    subprocess.Popen(["python", "tree_page1.py"])

treesb_picture_path = "treesb.png"
treesb_picture = resize_image(treesb_picture_path, 220, 90)
treesb_button = tk.Button(frame, image=treesb_picture, highlightthickness=0, relief='flat', borderwidth=0, command=open_trees)
treesb_button.grid(column=0, columnspan=2, row=1, pady=(200,0), sticky="n")

def open_queue():
    choose_window.destroy()
    subprocess.Popen(["python", "queue.py"])

queueb_picture_path = "queueb.png"
queueb_picture = resize_image(queueb_picture_path, 220, 90)
queueb_button = tk.Button(frame, image=queueb_picture, highlightthickness=0, relief='flat', borderwidth=0, command=open_queue)
queueb_button.grid(column=1, columnspan=2, row=1, pady=(200, 0), sticky="n")

button_picture_path_back = "back.png"
button_picture_back = resize_image(button_picture_path_back, 168, 40)
back_button = tk.Button(frame, image=button_picture_back, highlightthickness=0, relief='flat', borderwidth=0, command=what_DSA)
back_button.grid(column=2, row=1, padx=(0, 100), pady=(300, 0), sticky="se")

choose_window.mainloop()