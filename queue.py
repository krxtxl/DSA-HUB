import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)

root = tk.Tk()
root.geometry("1280x720")
root.configure(bg="#770f1a")

queuetitle = Image.open("QUEUETITLE.png")
queuetitle = queuetitle.resize((600, 155))
queuetitle = ImageTk.PhotoImage(queuetitle)

label = tk.Label(root, image=queuetitle, bg="#770f1a")
label.grid(column=0, row=0, sticky="nw")
label.place(x=-50, y=50)

text = tk.Text(root, width=90, height=20, wrap="word", font=("Arial Narrow", 25), fg="white", bg="#770f1a", bd=0, padx=0, pady=10)
text.place(x=60, y=240)

text.insert(tk.END, "is a data structure that follows the first in, first out.")
text.insert(tk.END, "\n")
text.insert(tk.END, "(FIFO) principle. It is a type of list where elements are")
text.insert(tk.END, "\n")
text.insert(tk.END, "added at one end, known as the rear, and removed")
text.insert(tk.END, "\n")
text.insert(tk.END, "from the other end, called the front. A real-world")
text.insert(tk.END, "\n")
text.insert(tk.END, "example of a queue is a line of people waiting at the")
text.insert(tk.END, "\n")
text.insert(tk.END, "bank. As each person enters, they are enqueued at")
text.insert(tk.END, "\n")
text.insert(tk.END, "the back of the line. When a teller is ready, a person is")
text.insert(tk.END, "\n")
text.insert(tk.END, "dequeued from the front of the line to be served.")
text.insert(tk.END, "\n")

def EXERCISE():
    root.destroy()
    subprocess.Popen(["python", "queue_practice.py"])

def back_choose():
    root.destroy()
    subprocess.Popen(["python", "choose_tab.py"])

queue = Image.open("QUEUE.png")
queue = queue.resize((400, 400))
queue = ImageTk.PhotoImage(queue)

image_label = tk.Label(root, image=queue, bg="#770f1a")
image_label.grid(column=0, row=0, padx=(800, 0), pady=(100, 0), sticky="w")

button_picture_path_practice = "practice.png"
button_picture_practice = resize_image(button_picture_path_practice, 168, 40)
practice_button = tk.Button(root, image=button_picture_practice, highlightthickness=0, relief='flat', borderwidth=0, command=EXERCISE)
practice_button.grid(column=0, row=0, padx=(1000, 0), pady=(550, 0), sticky="w")

button_picture_path_back = "back.png"
button_picture_back = resize_image(button_picture_path_back, 168, 40)
back_button = tk.Button(root, image=button_picture_back, highlightthickness=0, relief='flat', borderwidth=0, command=back_choose)
back_button.grid(column=0, row=0, padx=(1000, 0), pady=(650, 0), sticky="w")

root.mainloop()