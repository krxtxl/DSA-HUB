import tkinter as tk
from resize_image import resize_image
import subprocess

def next():
    root.destroy()
    subprocess.Popen(['python', 'tree_page2.py'])

def back():
    root.destroy()
    subprocess.Popen(['python', 'choose_tab.py']) #paedit nalang

#Initialize the main window
root = tk.Tk()
root.geometry("1280x720")
root.configure(bg="#770F1A")
root.title("Tree")

frame = tk.Frame(root, bg="#770F1A")
frame.pack(fill='both', expand=True)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

title_image_path = "images/trees_title.png"
title_image = resize_image(title_image_path, 600, 155)
title_image_label = tk.Label(frame, image=title_image, background="#770F1A")
title_image_label.grid(column=0, row=0, sticky='nw', pady=40)

text_description = (
    "A tree is an abstraction for a hiererchal structure. \n"
    "It is designed as a set of points called nodes and a set of lines \n"
    "called edges where an edge connects two distinct nodes.\n\n"
    "A tree has three properties: \n"
    "    ▻ One node is dsitinguished called a root.\n"
    "    ▻ Every node n other than the root is connected by an \n"
    "        edge to exactly one other node p closer to the root.\n"
    "    ▻ A tree is connected in the sense of that if we start at any \n"
    "        node n other than the root and move to the parent of n, \n"
    "        continue to the parent of the parent of n, and so on, we \n"
    "        eventually reach the root.\n"
    )

description_label = tk.Label(frame, 
                            text=text_description, 
                            font=("Arial Narrow", 18), 
                            fg='white',
                            bg='#770F1A', 
                            justify='left',
                            wraplength=600)
description_label.grid(column=0, row=1, sticky='w', padx=80)

icon_image_path = "images/tree_icon.png"
icon_image = resize_image(icon_image_path, 500, 500)
icon_image_label = tk.Label(frame, image=icon_image, background="#770F1A")
icon_image_label.grid(column=1, row=0, rowspan=3)

nxtbutton_image_path = "images/next.png"
nxtbutton_image = resize_image(nxtbutton_image_path, 168, 40)
nxtbutton_image_label = tk.Button(frame, 
                                image=nxtbutton_image, 
                                highlightthickness=0, 
                                relief='flat',
                                borderwidth=0, 
                                command=next)
nxtbutton_image_label.grid(column=1, row=2, sticky='e', padx=100)

backbutton_image_path = "images/back.png"
backbutton_image = resize_image(backbutton_image_path, 168, 40)
backbutton_image_label = tk.Button(frame, 
                                image=backbutton_image, 
                                highlightthickness=0, 
                                relief='flat',
                                borderwidth=0, 
                                command=back)
backbutton_image_label.grid(column=1, row=3, sticky='e', padx=100, pady=10)

root.mainloop()