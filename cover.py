import tkinter as tk
from resize_image import resize_image
import subprocess

def start():
    root.destroy()
    subprocess.Popen(['python', "whatDSA.py"])

#Main Window
root = tk.Tk()
root.geometry("1280x720")
root.configure(bg="#770F1A")
root.title("Cover")

#Frame
frame = tk.Frame(root, bg="#770F1A")
frame.pack(fill='x')

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

#Header
heading = tk.Label(frame,
                 text='DATA STRUCTURES AND ALGORITHM',
                 font=('Times New Roman', 18),
                 fg='white',
                 bg='#770F1A',
                 justify='left',
                 )
heading.grid(column=0, row=0, columnspan=3, padx=50, pady=50, sticky='nw')

title_underline = tk.Canvas(frame, width=1000, height=2, bg="white", highlightthickness=0)
title_underline.grid(row=0, column=0, sticky="new", columnspan=3, rowspan=2, pady=80, padx=50, )

#Body
##Left Pane
cover_image_path = "images/cover.png"
cover_image = resize_image(cover_image_path, 550, 500)
cover_image_label = tk.Label(frame, image=cover_image, background="#770F1A")
cover_image_label.grid(column=0, row=1, rowspan=2, padx=(50, 0), pady=30, sticky='w')

##Right Pane
#Title
title = tk.Label(frame,
                 text='DSA Hub: Dive\ninto Structures\nand Algorithms',
                 font=('Arial Narrow', 70),
                 fg='white',
                 bg='#770F1A',
                 justify='left')
title.grid(column=1, row=1, sticky='w')

#Start Button
startbutton_image_path = "images/start.png"
startbutton_image = resize_image(startbutton_image_path, 250, 60)
startbutton_image_label = tk.Button(frame, 
                                image=startbutton_image, 
                                highlightthickness=0, 
                                relief='flat',
                                borderwidth=0, 
                                command=start)
startbutton_image_label.grid(column=1, row=2, sticky='nw')

root.mainloop()