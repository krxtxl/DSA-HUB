import tkinter as tk
from resize_image import resize_image
import os
import subprocess

def open_practice():
    root.destroy()
    subprocess.Popen(["python", "tree_practice.py"])  

def back():
    root.destroy()
    subprocess.Popen(['python', 'tree_page1.py'])

root = tk.Tk()
root.geometry("1280x720")
root.configure(bg='#770F1A')
root.title('Tree')

frame = tk.Frame(root, bg="#770F1A")
frame.pack(fill='both', expand=True)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

title_image_path = "images/trees_title.png"
title_image = resize_image(title_image_path, 600, 155)
title_image_label = tk.Label(frame, image=title_image, background="#770F1A")
title_image_label.grid(column=0, row=0, sticky='nw', pady=(40, 10))

text_description = (
    "Parts of a Tree\n"
    "   1. Nodes - data objects (the circles) in a tree\n"
    "       a. A node has a key (used to identify them)\n"
    "       b. A payload (the actual data stored)\n"
    "   2. Edges - links between nodes (always pointing downward)\n\n"
    "Relationships\n"
    "   ▻ Parent - A is a parent of B\n"
    "   ▻ Child - B is a child of A\n"
    "   ▻ A node can only have one parent\n"
    "   ▻ If two nodes have the same parent they are siblings\n\n"
    "Names\n"
    "   ▻ Root - a node without a parent\n"
    "       ▻ Node A\n"
    "   ▻ Leaf - a node without a child(ren)\n"
    "       ▻ Nodes C, D, E, F\n"
    "   ▻ Subtree - a node and all of its descendants\n"
    )

description_label = tk.Label(frame, 
                            text=text_description, 
                            font=("Arial Narrow", 14), 
                            fg='white',
                            bg='#770F1A', 
                            justify='left',
                            wraplength=600)
description_label.grid(column=0, row=1, sticky='w', padx=80)

icon_image_path = "images/binary_tree.png"
icon_image = resize_image(icon_image_path, 500, 500)
icon_image_label = tk.Label(frame, image=icon_image, background="#770F1A")
icon_image_label.grid(column=1, row=0, rowspan=2, padx=80)

nxtbutton_image_path = "images/practice.png"
nxtbutton_image = resize_image(nxtbutton_image_path, 168, 40)
nxtbutton_image_label = tk.Button(frame, 
                                image=nxtbutton_image, 
                                highlightthickness=0, 
                                relief='flat',
                                borderwidth=0,
                                command=open_practice)
nxtbutton_image_label.grid(column=1, row=1, sticky='se', padx=100)

backbutton_image_path = "images/back.png"
backbutton_image = resize_image(backbutton_image_path, 168, 40)
backbutton_image_label = tk.Button(frame, 
                                image=backbutton_image, 
                                highlightthickness=0, 
                                relief='flat',
                                borderwidth=0, 
                                command=back)
backbutton_image_label.grid(column=1, row=2, sticky='e', padx=100, pady=10)

root.mainloop()