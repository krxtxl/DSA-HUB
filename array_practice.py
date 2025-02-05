import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess


def update_display():
    for i, lbl in enumerate(array_labels):
        lbl.config(text=array[i] if array[i] else "")


def get_value_type(value):
    try:
        return int(value), "int"
    except ValueError:
        try:
            return float(value), "float"
        except ValueError:
            return value, "str"


def check_type(value):
    if not array:
        return True
    first_element_type = type(array[0]).__name__
    return type(value).__name__ == first_element_type


def insert_element():
    try:
        index = int(index_entry.get())
        value = value_entry.get()
        converted_value, value_type = get_value_type(value)

        if not check_type(converted_value) and array[0] is not None:
            messagebox.showerror("Error", "Array elements must be of the same data type (int, float, or str).")
            return

        if 0 <= index < len(array):
            array[index] = converted_value
            update_display()
        else:
            messagebox.showerror("Error", "Index out of range!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Ensure the index is an integer.")


def delete_element():
    try:
        index = int(index_entry.get())
        if 0 <= index < len(array):
            array[index] = None
            update_display()
        else:
            messagebox.showerror("Error", "Index out of range!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Ensure the index is an integer.")


def search_element():
    value = value_entry.get()
    converted_value, value_type = get_value_type(value)

    if not check_type(converted_value) and array[0] is not None:
        messagebox.showerror("Error", "Search value type must match array element types.")
        return

    indices = [str(i) for i, v in enumerate(array) if v == converted_value]
    if indices:
        result_label.config(text=f"Found at indices: {', '.join(indices)}")
    else:
        result_label.config(text="Not found")


def try_again():
    index_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)
    result_label.config(text="")
    global array
    array = [None for _ in range(11)]
    update_display()


def go_back():
    root.destroy()
    subprocess.Popen(["python", "array.py"])


def resize_image(image_path, width, height):
    try:
        img = Image.open(image_path)
        img_resized = img.resize((width, height))
        return ImageTk.PhotoImage(img_resized)
    except FileNotFoundError:
        messagebox.showerror("Error", f"Image file not found: {image_path}")
        return None


root = tk.Tk()
root.title("Array Simulator")
root.geometry("1280x720")
root.configure(bg="#770f1a")

array = [None for _ in range(11)]

tk.Label(root, text="", bg="#770f1a", fg="white", font=("Arial", 30, "bold")).pack(padx=0)

try:
    img_path = "ARRAY.png"
    img = Image.open(img_path).resize((600, 155))
    img_tk = ImageTk.PhotoImage(img)
    tk.Label(root, image=img_tk, bg="#770f1a").pack(side="top", anchor="ne", padx=(0,680), pady=(25,0))
except:
    pass

array_frame = tk.Frame(root, bg="#770f1a")
array_frame.pack(pady=10)
array_labels = [tk.Label(array_frame, text="", width=8, height=3, bg="white", font=("Arial", 16), relief="solid") for _
                in range(11)]
for i, lbl in enumerate(array_labels):
    tk.Label(array_frame, text=f"[{i}]", bg="#770f1a", fg="white", font=("Arial", 14)).grid(row=0, column=i, padx=5)
    lbl.grid(row=1, column=i, padx=5)

input_frame = tk.Frame(root, bg="#770f1a")
input_frame.pack(pady=30)
tk.Label(input_frame, text="Index:", bg="#770f1a", fg="white", font=("Arial", 16)).grid(row=0, column=0, padx=10)
index_entry = tk.Entry(input_frame, width=8, font=("Arial", 16))
index_entry.grid(row=0, column=1, padx=10)

tk.Label(input_frame, text="Value:", bg="#770f1a", fg="white", font=("Arial", 16)).grid(row=0, column=2, padx=10)
value_entry = tk.Entry(input_frame, width=12, font=("Arial", 16))
value_entry.grid(row=0, column=3, padx=10)

button_frame = tk.Frame(root, bg="#770f1a")
button_frame.pack(pady=30)

insert_img_tk = resize_image("INSERT.png", 300, 80)
delete_img_tk = resize_image("DELETE.png", 300, 80)
search_img_tk = resize_image("SEARCH.png", 300, 80)

insert_button = tk.Button(button_frame, image=insert_img_tk, command=insert_element, bg="#770f1a", fg="white",
                          font=("Arial", 16), bd=0)
insert_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(button_frame, image=delete_img_tk, command=delete_element, bg="#770f1a", fg="white",
                          font=("Arial", 16), bd=0)
delete_button.grid(row=0, column=1, padx=10)

search_button = tk.Button(button_frame, image=search_img_tk, command=search_element, bg="#770f1a", fg="white",
                          font=("Arial", 16), bd=0)
search_button.grid(row=0, column=2, padx=10)

button_picture_path_practice = "tryagain.png"
button_picture_practice = resize_image(button_picture_path_practice, 168, 40)
if button_picture_practice:
    practice_button = tk.Button(
        root, image=button_picture_practice, highlightthickness=0, relief='flat',
        borderwidth=0, command=try_again, bg="#770f1a"
    )
    practice_button.place(x=1000, y=600)

button_picture_path_back = "back.png"
button_picture_back = resize_image(button_picture_path_back, 168, 40)
if button_picture_back:
    back_button = tk.Button(
        root, image=button_picture_back, highlightthickness=0, relief='flat',
        borderwidth=0, command=go_back, bg="#770f1a"
    )
    back_button.place(x=1000, y=650)

result_label = tk.Label(root, text="", bg="#770f1a", fg="white", font=("Arial", 18, "italic"))
result_label.pack(pady=20)

root.mainloop()