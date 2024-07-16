import tkinter as tk
from tkinter import ttk
import os

def Complete(title=None, path=None, center=True):
    if path is None or not os.path.exists(path):
        print("Invalid Path")
    else:
        print("The path exists.")
        
        




# Setup
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 5

window.title("Tkinter File Creator")
window.geometry(f'+{x}+{y}')
window.resizable(False, False)

# Widgets (you can add your widgets here)
label = ttk.Label(window, text="Tkinter App Creator!", font=("Arial", 18))
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

pathvar = tk.StringVar(value=r'C:\Users\micha\OneDrive\Pictures\Documents\VSCode Files\KindlingProjects\tkinter-Atlas')
path_label = ttk.Label(window, text="Path", font=("Arial", 12))
path_entry = ttk.Entry(window, width=20, textvariable=pathvar)
path_label.grid(row=1, column=0, padx=10, pady=(5,2))
path_entry.grid(row=1, column=1, padx=10)

titlevar = tk.StringVar(value=" ")
title_label = ttk.Label(window, text="Title",font=("Arial", 12))
title_entry = ttk.Entry(window, width=20, textvariable=titlevar)
title_label.grid(row=2, column=0, padx=10, pady=(5,2))
title_entry.grid(row=2, column=1, padx=10)

heightvar = tk.IntVar(value=800)
widthvar = tk.IntVar(value=600)
height_label = ttk.Label(window, text="Height", font=("Arial", 12))
height_entry = ttk.Entry(window, width=20, textvariable=heightvar)
height_label.grid(row=3, column=0, padx=10, pady=2)
height_entry.grid(row=3, column=1, padx=10)

width_label = ttk.Label(window, text="Width", font=("Arial", 12))
width_entry = ttk.Entry(window, width=20, textvariable=widthvar)
width_label.grid(row=4, column=0, padx=10, pady=2)
width_entry.grid(row=4, column=1, padx=10)

centervar = tk.BooleanVar(value=True)
centerbox = tk.Checkbutton(text="Centered", variable=centervar)
complete_button = ttk.Button(window, text='Submit', command=lambda: Complete(pathvar.get(), titlevar.get(), centervar.get()))
centerbox.grid(row=5, column=0, padx=10, pady=2)
complete_button.grid(row=5, column=1, padx=10, pady=10)

updatelabel = ttk.Label(window, text="Click Submit When Done", font=("Arial", 12))
updatelabel.grid(row=6, column=0, columnspan=2, padx=10, pady=2)



# Run
window.focus_force()
window.wm_attributes("-topmost", 1)
window.mainloop()