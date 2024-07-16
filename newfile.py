import tkinter as tk
from tkinter import ttk
import os

def Complete(path=None, title=None, center=True, updatelabel=None):
    if path is None or not os.path.exists(path):
        updatelabel.config(text="Invalid Path")
        return
    if title is None or title.strip() == "":
        updatelabel.config(text="Need Title")
        return
    updatelabel.config(text="Submitted Successfully")
    title  = '_'.join(title.strip().split())
    create_file(path, title, center)

def create_file(path, title, center):
    path = os.path.join(path, f'{title}.py')
    with open(path, 'w') as file:
        # Write some content to the file (optional)
        file.write("import tkinter as tk\nfrom tkinter import ttk\n\n# Setup\n")
        file.write("window = tk.Tk()\n")
        if center is None:
            pass
        else:
            file.write("screen_width = window.winfo_screenwidth()\n")
            file.write("screen_height = window.winfo_screenheight()\n")
            file.write("window_width = window.winfo_reqwidth()\n")
            file.write("window_height = window.winfo_reqheight()\n")
            file.write("x = (screen_width - window_width) // 2\n")
            file.write("y = (screen_height - window_height) // 2\n")
        file.write(f"window.title('{title}')\n")
        if center is None:
            file.write("window.geometry(f'{window_width}x{window_height}')\n")
        else:
            file.write("window.geometry(f'{window_width}x{window_height}+{x}+{y}')\n")
        file.write("window.resizable(False, False)\n\n# Widgets\n\n\n# Run\n")
        file.write("window.focus_force()\nwindow.wm_attributes('-topmost', 1)\nwindow.mainloop()")
    window.destroy()

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

pathvar = tk.StringVar(value="")
path_label = ttk.Label(window, text="Path", font=("Arial", 12))
path_entry = ttk.Entry(window, width=20, textvariable=pathvar)
path_label.grid(row=1, column=0, padx=10, pady=(5,2))
path_entry.grid(row=1, column=1, padx=10)

titlevar = tk.StringVar(value=" ")
title_label = ttk.Label(window, text="Title",font=("Arial", 12))
title_entry = ttk.Entry(window, width=20, textvariable=titlevar)
title_label.grid(row=2, column=0, padx=10, pady=(5,2))
title_entry.grid(row=2, column=1, padx=10)

updatelabel = ttk.Label(window, text="Click Submit When Done", font=("Arial", 12))
updatelabel.grid(row=4, column=0, columnspan=2, padx=10, pady=2)

centervar = tk.BooleanVar(value=True)
centerbox = tk.Checkbutton(text="Centered", variable=centervar)
complete_button = ttk.Button(window, text='Submit', command=lambda: Complete(pathvar.get(), titlevar.get(), centervar.get(), updatelabel))
centerbox.grid(row=3, column=0, padx=10, pady=2)
complete_button.grid(row=3, column=1, padx=10, pady=10)


# Run
title_entry.focus_force()
window.wm_attributes("-topmost", 1)
window.mainloop()