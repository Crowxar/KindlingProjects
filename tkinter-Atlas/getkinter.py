import tkinter as tk
from tkinter import ttk

# Button Func
def button_func():
    # Update label
    label.config(text=entry.get())
    entry.config(state='disabled', text="")
    button.config(state='disabled')
    reenable_button.config(state='enabled')

def reenable():
    label.config(text="Enter new text")
    entry.config(text=" ", state='enabled')
    button.config(state='enabled')
    reenable_button.config(state='disabled')



# Main Window
window = tk.Tk()
window.title("Getting and Setting widgets")


# Widgets
label = ttk.Label(window, text="Enter new text")
label.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text="Button", command=button_func)
button.pack()

reenable_button = ttk.Button(window, text="Re-Enable", state='disabled', command=reenable)
reenable_button.pack()

# Mainloop
window.mainloop()