import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)

def limit_input(event):
    current_text = entry.get()
    if len(current_text) > 10:
        entry.delete(10, tk.END)

def back_to_stack():
    practice_window.destroy()
    subprocess.Popen(["python", "stack.py"])

practice_window = tk.Tk()
practice_window.geometry("1280x720")
practice_window.configure(bg="#770F1A")
practice_window.title("Stack Practice")

frame = tk.Frame(practice_window, bg='#770F1A')
frame.pack(fill='both', expand=True)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

stack = []

def is_empty():
    return len(stack) == 0

def push_item():
    item = entry.get()
    if item and item != "TYPE SOMETHING...":
        stack.append(item)
        entry.delete(0, tk.END)
        update_stack_view()
        update_status(f"Pushed: {item}")

def pop_item():
    if not is_empty():
        item = stack.pop()
        update_stack_view()
        update_status(f"Popped: {item}")
    else:
        messagebox.showwarning("Warning", "Stack is empty!")

def peek_item():
    if not is_empty():
        item = stack[-1]
        update_status(f"Top item: {item}")
    else:
        messagebox.showinfo("Info", "Stack is empty!")

def update_stack_view():
    stack_listbox.delete(0, tk.END)
    for item in reversed(stack):
        centered_item = item.center(30)
        stack_listbox.insert(tk.END, centered_item)

def update_status(message):
    status_label.config(text=message)

def clear_stack():
    global stack
    stack = []
    update_stack_view()
    update_status("---Stack cleared!---")

title_image_path_1 = "stackname.png"
title_image_1 = resize_image(title_image_path_1, 600, 155)
title_image_label_1 = tk.Label(frame, image=title_image_1, bg="#770F1A")
title_image_label_1.image = title_image_1
title_image_label_1.grid(column=0, row=0, padx=(0, 0), pady=(50, 0), sticky="nw")

stack_listbox = tk.Listbox(
    frame,
    height=10,
    width=30,
    bg='#770F1A',
    fg='#FFFFFF',
    font=('Arial Narrow', 15, 'bold'),
    selectbackground='#770F1A',
    selectforeground='#FFFFFF',
    justify='center',
    highlightthickness=0
)
stack_listbox.grid(column=0, row=0, padx=(400, 0), pady=(200, 0), sticky="w")

stack_listbox.config(height=19)

entry = tk.Entry(frame, bg='#770F1A', font=('Arial Narrow', 12), width=50, bd=8,
                 relief='flat', highlightthickness=1, highlightbackground='#FFFFFF',
                 highlightcolor='#FFFFFF', fg="#FFFFFF", insertbackground='white')
entry.grid(column=1, row=0, padx=(0, 180), pady=(0, 200), sticky='e')
entry.insert(0, "TYPE SOMETHING...")
entry.bind("<FocusIn>", lambda event: entry.delete(0, tk.END) if entry.get() == "TYPE SOMETHING..." else None)
entry.bind("<FocusOut>", lambda event: entry.insert(0, "TYPE SOMETHING...") if entry.get() == "" else None)
entry.bind("<KeyRelease>", limit_input)

push_picture_path = "push.png"
push_picture = resize_image(push_picture_path, 220, 70)
push_button = tk.Button(frame, image=push_picture, highlightthickness=0, relief='flat', borderwidth=0, command=push_item)
push_button.grid(column=1, row=0, padx=(90, 0), pady=(100, 130), sticky="w")

pop_picture_path = "pop.png"
pop_picture = resize_image(pop_picture_path, 220, 70)
pop_button = tk.Button(frame, image=pop_picture, highlightthickness=0, relief='flat', borderwidth=0, command=pop_item)
pop_button.grid(column=1, row=0, padx=(90, 0), pady=(280, 130), sticky="w")

peek_picture_path = "peek.png"
peek_picture = resize_image(peek_picture_path, 220, 70)
peek_button = tk.Button(frame, image=peek_picture, highlightthickness=0, relief='flat', borderwidth=0, command=peek_item)
peek_button.grid(column=1, row=0, padx=(90, 0), pady=(430, 100), sticky="w")

recent_image_path = "recent.png"
recent_image = resize_image(recent_image_path, 280, 80)
recent_image_label = tk.Label(frame, image=recent_image, bg="#770F1A")
recent_image_label.image = recent_image
recent_image_label.grid(column=0, row=0, padx=(30, 0), pady=(60, 0), sticky="w")

status_label = tk.Label(frame, text="---Stack is ready!---", bg="#FFFBE0", fg="#000000", font=('Arial Narrow', 15, 'bold'))
status_label.grid(column=0, row=0, padx=(93, 0), pady=(90, 0), sticky="w")

button_picture_path_try = "tryagain.png"
button_picture_try = resize_image(button_picture_path_try, 168, 40)
try_button = tk.Button(frame, image=button_picture_try, highlightthickness=0, relief='flat', borderwidth=0, command=clear_stack)
try_button.grid(column=1, row=0, padx=(350, 0), pady=(550, 0), sticky="w")

button_picture_path_back = "back.png"
button_picture_back = resize_image(button_picture_path_back, 168, 40)
back_button = tk.Button(frame, image=button_picture_back, highlightthickness=0, relief='flat', borderwidth=0, command=back_to_stack)
back_button.grid(column=1, row=0, padx=(350, 0), pady=(650, 0), sticky="w")

practice_window.mainloop()