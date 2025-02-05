import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)

list = []

def is_empty():
    return len(list) == 0

def add_name():
    name = name_entry.get().strip()
    if name:
        listbox.insert(tk.END, name)
        name_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Name field cannot be empty.")

def remove_selected():
    selected_indices = listbox.curselection()
    if selected_indices:
        for i in reversed(selected_indices):
            listbox.delete(i)
    else:
        messagebox.showwarning("Selection Error", "No item selected.")

def clear_all():
    listbox.delete(0, tk.END)
    name_entry.delete(0, tk.END)

def back_list():
    root.destroy()
    subprocess.Popen(["python", "list.py"])

root = tk.Tk()
root.geometry("1280x720")
root.configure(bg="#770F1A")
root.title("List Generator")

frame = tk.Frame(root, bg='#770F1A')
frame.pack(fill='both', expand=True)

title_image_path_1 = "list_button.png"
title_image_1 = resize_image(title_image_path_1, 600, 155)
title_image_label_1 = tk.Label(frame, image=title_image_1, bg="#770F1A")
title_image_label_1.image = title_image_1
title_image_label_1.grid(column=0, row=0, padx=(0, 0), pady=(25, 0), sticky="nw")

title_image_path_2 = "list_name.png"
title_image_2 = resize_image(title_image_path_2, 200, 50)
title_image_label_2 = tk.Label(frame, image=title_image_2, bg="#770F1A")
title_image_label_2.image = title_image_2
title_image_label_2.grid(column=0, row=0, padx=(800, 0), pady=(75, 0), sticky="nw")

input_frame = tk.Frame(frame, bg='#770F1A', bd=2, borderwidth=2)
input_frame.grid(column=0, row=0, padx=(0, 250), pady=(0, 0))
input_frame.config(highlightbackground='white', highlightcolor='white', highlightthickness=2, height=100)

name_label = tk.Label(input_frame, text="Enter element/s:", font=("Ariel Narrow", 18), fg="white", bg="#770F1A")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, font=("Ariel Narrow", 18))
name_entry.grid(row=0, column=1, padx=5, pady=5)

add_button = "add.png"
add_try = resize_image(add_button, 168, 40)
add_button = tk.Button(input_frame, image=add_try, highlightthickness=0, relief='flat', borderwidth=0, command=add_name)
add_button.grid(column=1, row=1, padx=(50, 0), pady=(0, 0), sticky="w")

remove_button = "remove.png"
remove_try = resize_image(remove_button, 168, 40)
remove_button = tk.Button(input_frame, image=remove_try, highlightthickness=0, relief='flat', borderwidth=0, command=remove_selected)
remove_button.grid(column=1, row=2, padx=(50, 0), pady=(10, 0), sticky="w")

listbox = tk.Listbox(frame, height=20, width=30, bg='#fffbe0', fg='#000000', font=('Arial Narrow', 15, 'bold'),
                     selectbackground='#fffbe0', selectforeground='#000000', bd=0, relief='flat')
listbox.grid(column=0, row=0, padx=(600, 0), pady=(0, 0))
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)

button_picture_path_try = "tryagain.png"
button_picture_try = resize_image(button_picture_path_try, 168, 40)
try_button = tk.Button(frame, image=button_picture_try, highlightthickness=0, relief='flat', borderwidth=0, command=clear_all)
try_button.grid(column=1, row=0, padx=(0, 100), pady=(500, 0), sticky="w")

button_picture_path_back = "back.png"
button_picture_back = resize_image(button_picture_path_back, 168, 40)
back_button = tk.Button(frame, image=button_picture_back, highlightthickness=0, relief='flat', borderwidth=0,
                        command=root.destroy)
back_button.grid(column=1, row=0, padx=(0, 100), pady=(600, 0), sticky="w")

list_picture = "list.png"
button_picture_back = resize_image(button_picture_path_back, 168, 40)
back_button = tk.Button(frame, image=button_picture_back, highlightthickness=0, relief='flat', borderwidth=0, command=back_list)
back_button.grid(column=1, row=0, padx=(0, 20), pady=(600, 0), sticky="w")

root.mainloop()