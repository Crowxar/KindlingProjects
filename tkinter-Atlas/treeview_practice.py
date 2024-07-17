import tkinter as tk
from tkinter import ttk
from random import choice
import os

# Functions

# Data
first_names = [
    "John", "Jane", "Michael", "Emily", "David", "Sarah",
    "Robert", "Jessica", "James", "Laura", "William", "Olivia",
    "Daniel", "Sophia", "Matthew", "Emma", "Andrew", "Isabella",
    "Joseph", "Mia"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
    "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez",
    "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore",
    "Jackson", "Martin"
]

def item_select(_):
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    for i in table.selection():
        table.delete(i)


# Setup
window = tk.Tk()
window_width = 600
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 5
window.title('treeview_practice')
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
window.resizable(False, False)

# Widgets
table = ttk.Treeview(window, columns=('first','last','email'), show = 'headings')
table.heading('first', text = 'First Name')
table.heading('last', text = 'Last Name')
table.heading('email', text = 'E-Mail')
table.pack(fill='both', expand=True)

#table.insert(parent = '',index = 0, values=('John', 'Doe', 'JohnDoe@email.com'))

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}{last}@email.com'
    data = (first, last, email)
    table.insert(parent='', index = 0, values = data)

table.insert(parent="",index=tk.END,values=('xxx','yyy','zzz'))



# events
table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# Items

# Run
window.focus_force()
window.wm_attributes('-topmost', 1)
window.mainloop()
os.system('cls')