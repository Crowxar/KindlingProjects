import tkinter as tk
from tkinter import ttk
import os

# Functions
def get_pos(event):
    print(f'x: {event.x}, y: {event.y}')

# https://www.pythontutorial.net/tkinter/tkinter-event-binding/

# Setup
window = tk.Tk()
window_width = 600
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 5
window.title('event_testing')
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
window.resizable(False, False)

# Widgets
text = tk.Text(window, height = 8)
text.pack()

entry = tk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()

# Events
# button.bind('<Alt-KeyPress-a>', lambda event: print(event))
# window.bind('<KeyPress>', lambda event: print(f"Button was pressed({event.char})"))

#text.bind('<Motion>', get_pos)

# entry.bind('<FocusIn>', lambda event: print('entry was selected'))
# entry.bind('<FocusOut>', lambda event: print('entry was unselected'))

text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

# Run
window.focus_force()
window.wm_attributes('-topmost', 1)
window.mainloop()
os.system('cls')