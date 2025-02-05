import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
import os

def create_practice_window(root):
    root.destroy()
    try:
        practice_script = os.path.join(os.path.dirname(__file__), "array_practice.py")
        subprocess.Popen([sys.executable, practice_script])
    except Exception as e:
        print(f"Error launching practice script: {e}")

def back_choose(root):
    root.destroy()
    subprocess.Popen(["python", "choose_tab.py"])

def resize_image(image_path, width, height):
    try:
        image = Image.open(image_path)
        image = image.resize((width, height))
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image '{image_path}': {e}")
        return None

def create_window():
    root = tk.Tk()
    root.title("Array")
    root.geometry("1280x720")
    root.configure(bg="#770f1a")

    canvas = tk.Canvas(root, width=1280, height=720, bg="#770f1a", bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    title_image_path = "ARRAY.png"
    title_image = resize_image(title_image_path, 600, 155)
    if title_image:
        title_image_label = canvas.create_image(300, 100, image=title_image)
        canvas.image = title_image

    description1 = (
        "An Array is a collection of items stored at contiguous memory locations. "
        "It stores multiple items of the same type together, making it easier to calculate the position "
        "of each element based on the base value. Arrays are simple to implement and allow for efficient "
        "access (O(1) time) to any element. However, they have limitations such as a fixed size, making resizing "
        "difficult, and the need to shift elements during insertion or deletion operations."
    )

    description2 = (
        "Arrays are widely used in algorithms for sorting, searching, and dynamic programming, as well as in representing matrices and "
        "other multidimensional data structures. Arrays also support dynamic resizing and are essential for implementing data structures "
        "like stacks, queues, and hash tables. Their efficiency and versatility make them fundamental for solving a variety of algorithmic problems."
    )

    canvas.create_text(700, 210, text=description1, font=("Arial Narrow", 20), fill="white", width=680, anchor="ne")
    canvas.create_text(710, 450, text=description2, font=("Arial Narrow", 20), fill="white", width=680, anchor="ne")

    img_path_right = "ARRAY PICTURE.png"
    img_right = resize_image(img_path_right, 420, 420)
    if img_right:
        img_right_label = canvas.create_image(980, 390, image=img_right)
        canvas.image = img_right

    button_picture_path_practice = "practice.png"
    button_picture_practice = resize_image(button_picture_path_practice, 168, 40)
    if button_picture_practice:
        practice_button = tk.Button(
            root, image=button_picture_practice, highlightthickness=0, relief='flat',
            borderwidth=0, command=lambda: create_practice_window(root), bg="#770f1a"
        )
        practice_button.place(x=1000, y=600)

    button_picture_path_back = "back.png"
    button_picture_back = resize_image(button_picture_path_back, 168, 40)
    if button_picture_back:
        back_button = tk.Button(
            root, image=button_picture_back, highlightthickness=0, relief='flat',
            borderwidth=0, command=lambda: back_choose(root), bg="#770f1a"
        )
        back_button.place(x=1000, y=650)

    root.mainloop()

create_window()