import tkinter as tk
from tkinter import ttk

def button_func():
    print("Button Pressed")

def print_hello():
    print("Hello")

app = tk.Tk()
app.geometry('800x500')

# ttk label
label = ttk.Label(app, text='this is a test')
label.pack()

# tk text
text = tk.Text(app)
text.pack()

# ttk entry
entry = ttk.Entry(app)
entry.pack()

label2 = ttk.Label(app, text='My Label')
button2 = ttk.Button(app, text='Hello', command=print_hello)

label2.pack()
button2.pack()

# ttk button
button = ttk.Button(app, text='A Button', command=button_func)
button.pack()






app.mainloop()

import os
os.system('cls')