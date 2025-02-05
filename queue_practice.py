import tkinter as tk
from collections import deque
from PIL import Image, ImageTk
import subprocess

class QueueSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Simulation")
        self.root.geometry("1280x720")
        self.root.configure(bg="#770f1a")
        self.queue = deque()
        self.create_widgets()

    def create_widgets(self):
        def resize_image(image_path, width, height):
            image = Image.open(image_path)
            image = image.resize((width, height))
            return ImageTk.PhotoImage(image)

        self.title_label = tk.Label(self.root, text="Queue Simulation", font=("Arial Narrow", 60), fg="white", bg="#770f1a")
        self.title_label.place(x=395, y=60)

        self.entry_label = tk.Label(self.root, text="Enter an item to queue:", font=("Arial Narrow", 28), fg="white", bg="#770f1a")
        self.entry_label.place(x=495, y=180)

        self.entry = tk.Entry(self.root, font=("Arial Narrow", 28), width=20)
        self.entry.place(x=485, y=240)

        self.enqueue_button = tk.Button(self.root, text="Enqueue", font=("Arial Narrow", 20), command=self.enqueue, width=10, height=1, bd=1)
        self.enqueue_button.place(x=590, y=310)

        self.dequeue_button = tk.Button(self.root, text="Dequeue", font=("Arial Narrow", 20), command=self.dequeue, width=10, height=1, bd=1)
        self.dequeue_button.place(x=590, y=380)

        self.queue_label = tk.Label(self.root, text="Current Queue:", font=("Arial Narrow", 28), fg="white", bg="#770f1a")
        self.queue_label.place(x=100, y=440)

        self.queue_display = tk.Label(self.root, text="[ ]", font=("Arial Narrow", 20), fg="white", bg="#770f1a")
        self.queue_display.place(x=100, y=520)

        self.button_picture_path_try = "tryagain.png"
        self.button_picture_try = resize_image(self.button_picture_path_try, 168, 40)
        self.try_button = tk.Button(root, image=self.button_picture_try, highlightthickness=0, relief='flat', borderwidth=0,
                               command=self.reset)
        self.try_button.place(x=1000, y=600)

        self.button_picture_path_back = "back.png"
        self.button_picture_back = resize_image(self.button_picture_path_back, 168, 40)
        self.back_button = tk.Button(root, image=self.button_picture_back, highlightthickness=0, relief='flat', borderwidth=0,
                                command=self.go_back)
        self.back_button.place(x=1000, y=650)

    def enqueue(self):
        item = self.entry.get()
        if item:
            self.queue.append(item)
            self.entry.delete(0, tk.END)
            self.update_queue_display()

    def dequeue(self):
        if self.queue:
            self.queue.popleft()
            self.update_queue_display()

    def update_queue_display(self):
        self.queue_display.config(text=str(list(self.queue)))

    def reset(self):
        self.entry.delete(0, tk.END)
        self.queue.clear()
        self.update_queue_display()

    def go_back(self):
        self.root.destroy()
        subprocess.Popen(["python", "queue.py"])

root = tk.Tk()
app = QueueSimulation(root)
root.mainloop()
