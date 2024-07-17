import tkinter as tk
from tkinter import ttk
import os

# Functions
def button_func():
    print('A Simple Button')
    print(radio_var.get())

# Setup
window = tk.Tk()
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 5
window.title('button-variables')
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
window.resizable(False, False)

# Widgets
button_string = tk.StringVar(value="A Button with string var")
button = ttk.Button(window, text = "simple button", command = button_func, textvariable=button_string)
button.pack()

#checkbutton
check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(window,
                        text="Checkbox 1",
                        variable=check_var,
                        command=lambda: print(check_var.get()),
                        onvalue=10,
                        offvalue=5)
check.pack()


radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text='RadioButton1',
                         value='Radio1',
                         variable=radio_var,
                         command=lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window, text='RadioButton2',
                         value=2,
                         variable=radio_var,
                         command=lambda: print(radio_var.get()))
radio2.pack()



# Run
window.focus_force()
window.wm_attributes('-topmost', 1)
window.mainloop()
os.system('cls')
