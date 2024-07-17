import tkinter as tk
from tkinter import ttk
import os

# Functions


# Setup
window = tk.Tk()
window_width = 600
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 5
window.title('combo_box_testing')
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
window.resizable(False, False)

# Widgets
# Combobox
items = ('Ice Cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string, values=items)
combo.pack()

combo_label = ttk.Label(window, text='a label', font=("bold, 20"))
combo_label.pack()


# Spinbox
spin_int = tk.IntVar(value=1)
spin = ttk.Spinbox(
    window,
    from_ = 1, to = 20,
    increment = 1,
    textvariable= spin_int
    )
spin.pack()



# Events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f'Selected Value: {food_string.get()}'))
spin.bind('<<Increment>>', lambda event: print(f'up {spin_int.get()}'))
spin.bind('<<Decrement>>', lambda event: print(f'down {spin_int.get()}'))





# Run
window.focus_force()
window.wm_attributes('-topmost', 1)
window.mainloop()
os.system('cls')