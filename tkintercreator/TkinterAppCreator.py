import tkinter as tk
from tkinter import ttk, filedialog
import json
import re
import os


def save_default_path(path):
    data = {"default_path": path}
    with open("default_path.json", "w") as json_file:
        json.dump(data, json_file)


def load_default_path():
    try:
        with open("default_path.json", "r") as json_file:
            data = json.load(json_file)
            return data.get("default_path", "")
    except FileNotFoundError:
        return ""


def on_path_change():
    new_path = path_entry.get()
    save_default_path(new_path)


def browse_folder():
    folder_path = path_var.get()
    if folder_path:
        selected_folder = filedialog.askdirectory(initialdir=folder_path)
        if selected_folder:
            path_var.set(selected_folder)


def validate_format(value):
    value_stripped = value.strip()
    pattern = r"^\d+\s*x\s*\d+$"
    return bool(re.match(pattern, value_stripped))


def Complete(path=None, title=None, center=True, size=None, updatelabel=None):
    if path is None or not os.path.exists(path):
        updatelabel.config(text="Invalid Path")
        return
    if title is None or title.strip() == "":
        updatelabel.config(text="Need Title")
        return
    if size_var.get():
        size_tuple = ("window.winfo_reqwidth()", "window.winfo_reqheight()")
    else:
        size_bool = validate_format(size)
        if not size_bool:
            updatelabel.config(text="Invalid Size: Width x Height")
            return

        width_str, height_str = size.split("x")
        size_tuple = (int(width_str), int(height_str))

    updatelabel.config(text="Submitted Successfully")
    title = "_".join(title.lower().strip().split())
    on_path_change()
    create_file(path, title, center, size_tuple)


def create_file(path, title, center, size_tuple):
    path = os.path.join(path, f"{title}.py")
    with open(path, "w") as file:
        file.write(
            "import tkinter as tk\nfrom tkinter import ttk\nimport os\n\n#region ===Functions===\n\n\n#endregion\n\n#region ===Setup===\n"
        )
        file.write("window = tk.Tk()\n")
        if center is False:
            if size_tuple:
                file.write(f"window_width = {size_tuple[0]}\n")
                file.write(f"window_height = {size_tuple[1]}\n")
            else:
                file.write("window_width = window.winfo_reqwidth()\n")
                file.write("window_height = window.winfo_reqheight()\n")
        else:
            if size_tuple:
                file.write(f"window_width = {size_tuple[0]}\n")
                file.write(f"window_height = {size_tuple[1]}\n")
            else:
                file.write("window_width = window.winfo_reqwidth()\n")
                file.write("window_height = window.winfo_reqheight()\n")
            file.write("screen_width = window.winfo_screenwidth()\n")
            file.write("screen_height = window.winfo_screenheight()\n")
            file.write("x = (screen_width - window_width) // 2\n")
            file.write("y = (screen_height - window_height) // 5\n")
        file.write(f"window.title('{title}')\n")
        if center is False:
            file.write("window.geometry(f'{window_width}x{window_height}')\n")
        else:
            file.write("window.geometry(f'{window_width}x{window_height}+{x}+{y}')\n")
        file.write("window.resizable(False, False)\n\n#endregion\n\n#region ===Widgets===\n\n\n#endregion\n\n#region ===Run===\n")
        file.write(
            "window.focus_force()\nwindow.wm_attributes('-topmost', 1)\nwindow.mainloop()\nos.system('cls')\n#endregion\n"
        )
    window.destroy()


def toggle_entry_state():
    if size_var.get():  # If checkbutton is checked
        size_entry.config(state=tk.DISABLED)
        size_entry.insert(0, "Width x Height")
    else:
        size_entry.config(state=tk.NORMAL)
        size_entry.delete(0, tk.END)


window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 5

window.title("Tkinter File Creator")
window.geometry(f"+{x}+{y}")
window.resizable(False, False)

label = ttk.Label(window, text="Tkinter App Creator!", font=("Arial", 18))
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

default_path = load_default_path()
if default_path:
    path_var = tk.StringVar(value=default_path)
else:
    path_var = tk.StringVar(value=os.getcwd())

path_entry = ttk.Entry(window, width=20, textvariable=path_var)
path_button = tk.Button(window, text="Path Browse", command=browse_folder)

path_button.grid(row=1, column=0, padx=10, pady=(5, 2))
path_entry.grid(row=1, column=1, padx=10)

titlevar = tk.StringVar(value="")
title_label = ttk.Label(window, text="Title", font=("Arial", 12))
title_entry = ttk.Entry(window, width=20, textvariable=titlevar)
title_label.grid(row=2, column=0, padx=10, pady=(5, 2))
title_entry.grid(row=2, column=1, padx=10)

size_var = tk.BooleanVar(value=True)
size_box = tk.Checkbutton(
    text="Auto Size", variable=size_var, command=toggle_entry_state
)
basic_size = tk.StringVar(value="Width x Height")
size_entry = ttk.Entry(window, width=20, textvariable=basic_size, state=tk.DISABLED)
size_box.grid(row=3, column=0, padx=10, pady=(5, 2))
size_entry.grid(row=3, column=1, padx=10)

updatelabel = ttk.Label(window, text="Click Submit When Done", font=("Arial", 12))
updatelabel.grid(row=5, column=0, columnspan=2, padx=10, pady=2)

centervar = tk.BooleanVar(value=True)
centerbox = tk.Checkbutton(text="Centered", variable=centervar)
complete_button = ttk.Button(
    window,
    text="Submit",
    command=lambda: Complete(
        path_var.get(), titlevar.get(), centervar.get(), basic_size.get(), updatelabel
    ),
)
centerbox.grid(row=4, column=0, padx=10, pady=2)
complete_button.grid(row=4, column=1, padx=10, pady=10)

title_entry.bind("<Return>", lambda event: complete_button.invoke())
title_entry.focus_force()
window.wm_attributes("-topmost", 1)
window.mainloop()
