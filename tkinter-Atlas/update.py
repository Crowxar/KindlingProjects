import tkinter as tk
from tkinter import ttk


#Functions
def button_fun():
    print(string_var.get())
    string_var.set("Button Pressed")
    clicker.set(clicker.get() + 1)

#Window
window = tk.Tk()
window.title('Tkinter Variables')

#Tkinter Variable
string_var = tk.StringVar()
clicker = tk.IntVar(value=0)


#Widgets
label = ttk.Label(window, text='Label', textvariable= string_var)
label.pack()

entry = ttk.Entry(window, textvariable= string_var)
entry.pack()


button = ttk.Button(window, textvariable=f'{clicker}', command=button_fun)
button.pack()


#Run
window.mainloop()