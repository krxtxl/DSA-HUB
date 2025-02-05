import tkinter as tk
from resize_image import resize_image
import subprocess

# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Binary Search Tree class
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if not current.left:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif value > current.value:
            if not current.right:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            min_value = self._find_min(node.right)
            node.value = min_value
            node.right = self._delete(node.right, min_value)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.value

# Visualization with Tkinter
class BSTVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("BST Visualization")
        self.bst = BST()
        self.root.geometry('1280x720')
        self.root.configure(bg='#770F1A')

        #Title
        self.title_image_path = "images/trees_title.png"
        self.title_image = resize_image(self.title_image_path, 600, 155)
        self.title_image_label = tk.Label(self.root, image=self.title_image, background="#770F1A")
        self.title_image_label.grid(column=0, row=0, sticky='nw', pady=40)

        #Title of Practice
        self.prac_title = tk.Label(root,
                                   text='Binary Tree Maker', 
                                    font=("Arial Narrow", 30, 'bold'), 
                                    fg='white',
                                    bg='#770F1A')
        self.prac_title.grid(column=1, row=1, sticky='n')

        # Input Frame
        self.input_frame = tk.Frame(root)
        self.input_frame.configure(bg='#770F1A')
        self.input_frame.grid(column=1, row=1, padx=80)

        ##Images for Entry
        self.insert_image_path = "images/insert.png"
        self.insert_image = resize_image(self.insert_image_path, 100, 30)

        self.delete_image_path = "images/delete.png"
        self.delete_image = resize_image(self.delete_image_path, 100, 30)

        self.entry = tk.Entry(self.input_frame, width=20, background='#fffbe0', font=('Arial', 20), relief="solid", justify="center")
        self.entry.grid(column=0, row=0, columnspan=2, pady=10)
        self.insert_button = tk.Button(self.input_frame, image=self.insert_image, command=self.insert_node, relief='flat')
        self.insert_button.grid(column=0, row=1, sticky='e', padx=5)
        self.delete_button = tk.Button(self.input_frame, image=self.delete_image, command=self.delete_node, relief='flat')
        self.delete_button.grid(column=1, row=1, sticky='w')

        # Canvas for tree visualization
        self.canvas = tk.Canvas(root, width=800, height=400, bg="#770F1A")
        self.canvas.configure(borderwidth=0, border=None)
        self.canvas.grid(column=0, row=1, padx=20)

        #Try Again and Back Button
        self.againbutton_image_path = "images/try again.png"
        self.againbutton_image = resize_image(self.againbutton_image_path, 168, 40)
        self.againbutton_image_label = tk.Button(root, 
                                        image=self.againbutton_image, 
                                        highlightthickness=0, 
                                        relief='flat',
                                        borderwidth=0, 
                                        command=self.reset)
        self.againbutton_image_label.grid(column=1, row=1, sticky='se', padx=100, pady=10)

        self.backbutton_image_path = "images/back.png"
        self.backbutton_image = resize_image(self.backbutton_image_path, 168, 40)
        self.backbutton_image_label = tk.Button(root, 
                                        image=self.backbutton_image, 
                                        highlightthickness=0, 
                                        relief='flat',
                                        borderwidth=0, 
                                        command=self.back)
        self.backbutton_image_label.grid(column=1, row=2, sticky='ne', padx=100)

    def insert_node(self):
        try:
            value = int(self.entry.get())
            self.bst.insert(value)
            self.entry.delete(0, tk.END)
            self.draw_tree()
        except ValueError:
            pass

    def delete_node(self):
        try:
            value = int(self.entry.get())
            self.bst.delete(value)
            self.entry.delete(0, tk.END)
            self.draw_tree()
        except ValueError:
            pass

    def draw_tree(self):
        self.canvas.delete("all")
        if self.bst.root:
            self._draw_node(self.bst.root, 400, 50, 100)

    def _draw_node(self, node, x, y, x_offset):
        if node.left:
            self.canvas.create_line(x, y, x - x_offset, y + 50, fill="white")
            self._draw_node(node.left, x - x_offset, y + 50, x_offset // 2)

        if node.right:
            self.canvas.create_line(x, y, x + x_offset, y + 50, fill="white")
            self._draw_node(node.right, x + x_offset, y + 50, x_offset // 2)

        # Draw the current node
        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#fffbe0")
        self.canvas.create_text(x, y, text=str(node.value), font=("Arial", 12))

    def back(self):
        self.root.destroy()
        subprocess.Popen(['python', 'tree_page2.py'])

    def reset(self):
        self.entry.delete(0, tk.END)
        self.bst = BST()
        self.canvas.delete("all")
        self.draw_tree()


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = BSTVisualizer(root)
    root.mainloop()
